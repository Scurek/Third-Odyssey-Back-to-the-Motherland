"""
Scrape the localisation files and search if and where they're used, based on pure regex text search.

Author: lichtkang
"""

import sys

if sys.version_info < (3, 9):
    sys.exit("Needs Python 3.9 or higher")

import os
import json
import pathlib
import logging
import logging.handlers
import datetime
import functools
import collections
import typing as t


# -- Globals --

# Directory of the mod. Change this if needed. Assuming certain relative positions of script to files.
MOD_DIR = pathlib.Path(__file__).absolute().parent.parent.parent.joinpath('deploy')
LOGS_DIR = 'logs'
STATSDIR = 'stats'
OUTDIR = 'output'
# Subdirectories within the mod to exclude from search
EXCLUDED_SUBDIRS = [
    'localisation',  # Of course, if we don't exclude localisation, we'll find all!
    'gfx',
    'history',
    'interface',
    'sound',
    'common/units',  # Contain no localisation
    'common/countries',  # Contain no localisation
]
EXCLUDED_LOCFILES = [
    'xxx_manually_verified_l_english.yml',  # A localisation file that should contain 'manually' verified
]
CAT_SORT_BY_APPEARANCE = [
    'events',
]
CAT_VARIANTS_PREFIX_SUFFIX_MAP = {
    'common/event_modifiers': [('desc_', ''), ],
    'common/triggered_modifiers': [('desc_', '')],
    'common/province_triggered_modifiers': [('desc_', ''), ],
    'decisions': [('', '_desc'), ('', '_title')],
    'common/tradegoods': [('', 'DESC')],
    'common/governments': [
        ('', '_desc'),
        ('', '_name'),
    ],
    'common/government_names': [
        # Note: not all of these may still be used in current EU4
        ('', '_desc'),
        ('', '_ruler'),
        ('', '_ruler_female'),
        ('', '_vassal'),
        ('', '_ruler_vassal'),
        ('', '_long_desc'),
        ('', '_is_our'),
        ('', '_title'),
        ('', '_title_plural')
    ],
    'common/subject_types': [
        # Note: Assume same as government names?
        ('', '_desc'),
        ('', '_ruler'),
        ('', '_ruler_female'),
        ('', '_vassal'),
        ('', '_ruler_vassal'),
        ('', '_long_desc'),
        ('', '_is_our'),
        ('', '_title'),
        ('', '_title_plural'),
    ],
    'common/rebel_types': [
        ('', '_army'),
        ('', '_name'),
        ('', '_title'),
        ('', '_desc'),
        ('', '_demand_desc'),
    ],
    'common/ideas': [('', '_start'), ('', '_bonus'), ('', '_desc')],
    'common/country_tags': [('', '_ADJ')],
    'common/personal_deities': [('', '_desc')],
    'common/estates': [('', '_desc')],
    'common/estate_privileges': [('', '_desc')],
    'missions': [('', '_desc'), ('', '_title')],
    'common/factions': [('', '_FACTION_DESC'), ('', '_influence')],
    'common/government_reforms': [('', '_desc')],
    'common/peace_treaties': [
        ('', '_desc'),
        ('PEACE_', ''),
        ('CB_ALLOWED_', ''),
    ],
    'common/cb_types': [('', '_desc')],
    'common/policies': [('desc_', '')],
    'common/religions': [
        ('desc_', ''),  # Orthodox icons are in religion file, description localisations preceded by 'desc_'
        ('', '_religion_desc'),
    ],
    'common': [
        ('desc_', ''),  # Tech groups in common/technology.txt
        ('', '_desc'),  # Tech groups in common/technology.txt
    ],
    'common/technologies': [
        ('', 'DESCR'),  # Unit types are present in military techs
    ],
    'common/advisortypes': [('', '_desc')],
    'common/disasters': [('', '_desc')],
    'common/new_diplomatic_actions': [('', '_title'), ('', '_desc'), ('', '_tooltip')],
    'common/flagship_modifications': [('', '_desc')],
    'common/great_projects': [('great_project_', '')]
}

CAT_PRIORITIES_MAP = {
    # Greater values -> later in sorting (sorting defaults to ascending order)
    'common/country_tags': -140,
    'common': -130,  # Graphical culture type, technologies
    'common/tradegoods': -120,
    'common/religions': -116,  # Referred to in personal_deities
    'common/personal_deities': -115,  # Some names in cultures are deities
    'common/cultures': -110,
    'common/opinion_modifiers': -102,
    'common/province_modifiers': -101,
    'common/event_modifiers': -100,
    'common/ideas': -90,
    'common/subject_types': -80,
    'common/government_names': -75,
    'common/government_reforms': -74,
    'common/governments': -73,
    'common/estates': -70,
    'common/estate_privileges': -69,
    'common/disasters': -60,
    'common/triggered_modifiers': 90,  # May contain all kinds of stuff
    'events': 100,  # May contain all kinds of stuff  (NOTE: maybe not an issue to put at latest, since event localisations != unlocalised event identifier?)
    'decisions': 110,  # May trigger events and contain all kinds of conditions
    'missions': 120,  # May trigger events and contain all kinds of conditions  (NOTE: are missions used as conditions?)
    'common/on_actions': 130,  # Contains no localisation itself
}
GROUP_MIN_SIZE = 6  # Minimum size of groups, when sorting by group


# -- Logging --

def log_setup(logs_dir: str):
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H_%M_%S")
    log_handler = logging.FileHandler(f'{logs_dir}/{timestamp}.log', mode='w', encoding='utf-8')
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)


# -- Classes --

class LocId:

    _VALID_VAR_CHARS = '._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, identifier: str, text: str, sourcename: str):
        """Localisation identifier utility class. """
        self.identifier = identifier
        self.text = text
        self.sourcename = sourcename

    def find_usage(self, content: str, category: str) -> t.Optional[t.Tuple[int, int]]:
        """
        Find if the localisation identifier is in content.

        :param content: the entire data to parse
        :param category: content category, used to determine identifier variants
        :return: the line at which the localisation was found, or None if not found
        """
        variants = [self.identifier, ] + self.get_varientnames(identifier=self.identifier, category=category)
        for variant in variants:
            result = self._find_usage(identifier=variant, content=content)
            if result is not None:
                return result
        return None

    # -- Internal Methods --

    @classmethod
    @functools.cache
    def get_varientnames(cls, identifier: str, category: str) -> list[str]:
        """Cached version of `_determine_variantnames`, specific for this instance."""
        return cls._determine_variantnames(identifier=identifier, category=category)

    @classmethod
    def _find_usage(cls, identifier: str, content: str) -> t.Optional[t.Tuple[int, int]]:
        idx = -1
        while True:
            idx = content.find(identifier, idx+1)
            if idx == -1:
                break  # Not found
            before_idx, after_idx = idx-1, idx+len(identifier)
            before = content[before_idx] if before_idx >= 0 else ' '
            after = content[after_idx] if after_idx < len(content) else ' '
            if before in cls._VALID_VAR_CHARS or after in cls._VALID_VAR_CHARS:
                continue  # Character before or after extends the identifier => not exact 'word' match
            preceding_comment_idx = content.rfind('#', 0, idx)
            preceding_newline_idx = content.rfind('\n', 0, idx)
            if preceding_comment_idx != -1 and preceding_comment_idx > preceding_newline_idx:
                continue  # Preceded by comment (in the same line)
            line_nr = content.count('\n', 0, idx) + 1
            line_start_idx = content.rfind('\n', 0, idx)
            line_start_idx = line_start_idx if line_start_idx != -1 else 0  # For first line, line starts at 0
            indents = content.count('\t', line_start_idx, idx)
            return line_nr, indents
        return None

    @classmethod
    def _determine_variantnames(cls, identifier: str, category: str) -> list[str]:
        """Determine the variant names of a localisation string"""
        prefix_suffix_list = CAT_VARIANTS_PREFIX_SUFFIX_MAP.get(category, [])
        variants = []
        for prefix, suffix in prefix_suffix_list:
            variant = identifier.removeprefix(prefix).removesuffix(suffix)
            if variant != identifier:
                variants.append(variant)
        return variants


class SubjectFile:

    def __init__(self, subjname: str, content: str, category: str):
        """Subject file utility class."""
        self.subjname = subjname
        self.content = content
        self.category = category

    def search_locids(self, locids: t.Sequence['LocId']) -> t.Generator[tuple['LocId', int, int], None, None]:
        """
        Search the file content for the presence of localisation identifiers.

        :param locids: localisation identifiers
        """
        for locid in locids:
            findings = locid.find_usage(content=self.content, category=self.category)
            if findings is not None:
                line_nr, indents = findings
                yield locid, line_nr, indents


class SearchStats:

    def __init__(self, locids: list['LocId']):
        """Localisation search statistics data class. """
        # Internal reference data
        self._locids_map: dict[str, 'LocId'] = {locid.identifier: locid for locid in locids}
        self._sources_all_ids: dict[str, set] = collections.defaultdict(set)
        for locid in locids:
            self._sources_all_ids[locid.sourcename].add(locid.identifier)
        # Tracked stats
        self.category_subjname_matches_map: dict[str, dict[str, dict[str, t.Tuple[int, int]]]] = collections.defaultdict(lambda: collections.defaultdict(dict))  # category -> [subjname -> [identifier -> (line_nr, indents)]]
        self.locid_matchlist_map: dict[str, t.List[t.Tuple[str, str, int, int]]] = collections.defaultdict(list)  # identifier -> [List of (category, subjname, line_nr, indents)]
        self.sources_finds_map: dict[str, dict[str, str]] = collections.defaultdict(dict)  # sourcename -> [identifier -> subjname]
        self.found_ids: set[str] = set()
        self.missing_ids = set(self._locids_map.keys())

    @property
    def found(self) -> int:
        return len(self.found_ids)

    @property
    def missing(self) -> int:
        return len(self.missing_ids)

    @property
    def total(self) -> int:
        return len(self._locids_map)

    # -- Public Methods --

    def add(self, subjname: str, category: str, line_nr: int, indents: int, locid: 'LocId') -> None:
        """
        Add a found localisation.

        :param subjname: name for the subject
        :param category: the category the subject belongs to
        :param line_nr: number of the line in the subject at which the localisation was found
        :param indents: number of indents of the line at which the localisation was found
        :param locid: the found localisation identifier instance
        """
        self.category_subjname_matches_map[category][subjname][locid.identifier] = (line_nr, indents)
        self.locid_matchlist_map[locid.identifier].append((category, subjname, line_nr, indents))
        self.sources_finds_map[locid.sourcename][locid.identifier] = subjname
        self.found_ids.add(locid.identifier)
        self.missing_ids.discard(locid.identifier)

    def write_subj_data(self, fh: t.TextIO):
        """Output subjects localisation data in JSON format to the given filehandle."""
        json.dump(
            obj=self.category_subjname_matches_map,
            fp=fh,
            indent='\t',
        )

    def write_sources_stats(self, fh: t.TextIO):
        """Output localisation sources statistics in TSV format to the given filehandle."""
        locfile_stats = []
        for sourcename, all_locs in self._sources_all_ids.items():
            found_locs = self.sources_finds_map[sourcename]
            locfile_stats.append((
                sourcename,
                len(found_locs)/len(all_locs),  # Usage
                len(all_locs),  # Total identifiers
            ))
        locfile_stats.sort(key=lambda x: x[1])  # Sort from lowest to highest usage
        fh.write('Source\tUsage\tTotal\n')
        for filename, perc_used, total in locfile_stats:
            fh.write(f"{filename}\t{perc_used:.0%}\t{total}\n")

    def write_unused_locs(self, fh: t.TextIO):
        """Output unused localisation in PDX YAML format to the given filehandle."""
        fh.write('l_english:\n')
        for identifier in sorted(self.missing_ids):
            text = self._locids_map[identifier].text
            fh.write(f' {identifier}:0 {text}\n')

    def write_used_locs(self, outdir: str):
        """Output used localisations in PDX YAML format to various files."""
        # Get best match per localisation
        locid_best_match_map = {
            identifier: min(matches, key=self._match_key_func)
            for identifier, matches in self.locid_matchlist_map.items()
            if matches
        }
        # Group into files for writing
        outpath_locids_map: t.Dict[str, t.List[str]] = collections.defaultdict(list)
        for identifier, match in locid_best_match_map.items():
            outpath = self._get_output_locfile_path(outdir=outdir, match=match)
            outpath_locids_map[outpath].append(identifier)
        # Output to files
        for outpath, locids in outpath_locids_map.items():
            category = locid_best_match_map[locids[0]][0]  # Category for the entire file should be category of all localisations (?)
            sort_by_appearance = category in CAT_SORT_BY_APPEARANCE
            # Group localisations
            group_locids_map = self._group_locids(locids=locids, locid_match_map=locid_best_match_map)
            # Sort localisation groups
            for group_locids in group_locids_map.values():
                group_locids.sort(key=lambda identifier: self._identifier_key_func(
                    identifier=identifier, match=locid_best_match_map[identifier], by_appearance=sort_by_appearance
                ))
            # Write all to file
            with open(outpath, 'w', encoding='utf-8') as fh:
                fh.write('l_english:\n')
                # Write ungrouped
                for identifier in group_locids_map.pop('', []):
                    text = self._locids_map[identifier].text
                    fh.write(f' {identifier}:0 {text}\n')
                # Write groups alphabetically
                for group in sorted(group_locids_map.keys()):
                    group_locids = group_locids_map[group]
                    fh.write(f"\n # {group}\n")
                    for identifier in group_locids:
                        text = self._locids_map[identifier].text
                        fh.write(f' {identifier}:0 {text}\n')

    # -- Internal Methods --

    @staticmethod
    def _match_key_func(match: t.Tuple[str, str, int, int]) -> tuple:
        """Get the key by which to sort a match for finding the most relevant match, from: category, subjname, line_nr, indent."""
        # Sorting by tuples: first item is used for sorting first, on draws, second item is used etc.
        # Here: indent, category priority, category (alphabetical)
        return match[3], CAT_PRIORITIES_MAP.get(match[0], 0), match[0]

    @staticmethod
    def _get_output_locfile_path(outdir: str, match: t.Tuple[str, str, int, int]) -> str:
        """Get the localisation output file path suited for a localisation with the given match. """
        category, subjname, line_nr, indents = match
        outpath = f"{outdir}/{category.split('/')[-1]}_l_english.yml"
        return outpath

    @staticmethod
    def _group_locids(locids: t.List[str], locid_match_map: t.Dict[str, t.Tuple[str, str, int, int]]) -> t.Dict[str, t.List[str]]:
        """Get the group to which a localisation belongs."""
        # Group by subject name
        group_locids_map = collections.defaultdict(list)
        for identifier in locids:
            match = locid_match_map[identifier]
            group = match[1]  # Subjname
            group_locids_map[group].append(identifier)
        # Dissolve small groups to the 'ungrouped' group
        dissolve_groups = [group for group, locids in group_locids_map.items() if len(locids) < GROUP_MIN_SIZE]
        for group in dissolve_groups:
            group_locids_map[''].extend(group_locids_map.pop(group))
        return group_locids_map

    @staticmethod
    def _identifier_key_func(identifier: str, match: t.Tuple[str, str, int, int], by_appearance=False) -> tuple:
        """Get the key by which to sort an identifier within an output file, the match data: category, subjname, line_nr, indent."""
        category, subjname, line_nr, indent = match
        if by_appearance:
            return line_nr,
        else:
            all_variants = [identifier, ] + LocId.get_varientnames(identifier=identifier, category=category)
            shortest_variant = min(all_variants, key=lambda variant: len(variant))
            return shortest_variant,


# -- Public Methods --

def locids_from_filepath(filepath: str, sourcename: str) -> list['LocId']:
    """Get localisation identifiers from a source file. Logs file corruption."""
    results = []
    with open(filepath, 'r', encoding='utf-8') as fh:
        fh.readline()  # Skip first line, which specifies language
        for line_nr, line in enumerate(fh, start=2):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                identifier, text = line.strip().split(':0', 1)
            except ValueError:
                # Too few variables to unpack (corrupt), skip
                logging.warning(f"Corruption in localisation file '{os.path.basename(filepath)}', line {line_nr}")
                continue
            else:
                results.append(LocId(identifier=identifier, text=text, sourcename=sourcename))
    return results


def filter_duplicate_locids(locids: list['LocId']) -> None:
    """Remove duplicate localisation identifiers from the input. Logs every removal."""
    # Simply removing duplicates would be faster by implementing __hash__ and __eq__ and putting into a set,
    #  But we also want to report duplicates.
    idx = 0
    locids.sort(key=lambda x: x.identifier)  # Sort by identifier: fast. Duplicates will always be subsequent.
    while idx < len(locids) - 1:
        current = locids[idx]
        while (idx < len(locids) - 1) and (locids[idx+1].identifier == current.identifier):
            logging.warning(f"Duplicate localisation identifier: {current.identifier} ('{current.sourcename}' and '{locids[idx+1].sourcename}')")
            locids.pop(idx+1)
        idx += 1


def subjfile_from_filepath(filepath: str, mod_dirpath: str) -> 'SubjectFile':
    """Get subject file instance from a file in the mod directory"""
    # Note: it seems PDX uses *an* ANSI type encoding (probably cp1252?), rather than UTF-8.
    with open(filepath, 'r', encoding='cp1252') as fh:
        content = fh.read()
    category = os.path.relpath(os.path.dirname(filepath), mod_dirpath).lower().replace('\\', '/')
    return SubjectFile(
        subjname=os.path.basename(filepath),
        content=content,
        category=category
    )


# -- Run as Script --

def _load_subjfiles(mod_dirpath: str, excluded_subdirs: list[str]) -> list['SubjectFile']:
    """Load all subject files from the mod directory."""
    results = []
    excluded_subdirs = {os.path.join(mod_dirpath, *subdir.lower().split('/')) for subdir in excluded_subdirs}
    for root, dirs, files in os.walk(mod_dirpath):
        if root in excluded_subdirs:
            dirs.clear()
            continue
        results.extend([
            subjfile_from_filepath(filepath=os.path.join(root, filename), mod_dirpath=mod_dirpath)
            for filename in files
            if filename.endswith('.txt')
        ])
    return results


def _load_locids(loc_dirpath: str) -> list['LocId']:
    """Load all localisation identifiers from the given localisations directory."""
    locids = []
    # Get locids from all english localisatino files
    for filename in os.listdir(loc_dirpath):
        filepath = os.path.join(loc_dirpath, filename)
        if not filename.endswith('l_english.yml'):
            continue
        if filename in EXCLUDED_LOCFILES:
            continue
        locids.extend(locids_from_filepath(filepath=filepath, sourcename=filename))
    # Filter duplicates and return
    filter_duplicate_locids(locids=locids)
    return locids


def get_stats(mod_dirpath: str, subjfile_data_filepath: str) -> SearchStats:
    """Get stats from a stats subject file data dump and mod localisation source."""
    locids = _load_locids(loc_dirpath=os.path.join(mod_dirpath, 'localisation'))
    locids_map = {locid.identifier: locid for locid in locids}
    logging.info(f"Localisation identifiers count: {len(locids)}")
    stats = SearchStats(locids=locids)
    # Load localisations from stats dump
    with open(subjfile_data_filepath, 'r', encoding='utf-8') as fh:
        data: t.Mapping[str, t.Mapping[str, t.Mapping[str, t.Tuple[int, int]]]] = json.load(fh)  # Category -> [Subject name -> [identifier -> line_nr]]
        for category, subjfile_matches_map in data.items():
            for subjname, matches_map in subjfile_matches_map.items():
                for identifier, findings in matches_map.items():
                    line_nr, indents = findings
                    stats.add(subjname=subjname, category=category, line_nr=line_nr, indents=indents, locid=locids_map[identifier])
    return stats


def search_stats(mod_dirpath: str, excluded_subdirs: list[str]) -> SearchStats:
    """Search for localisation data and statistics in a mod directory."""
    locids = _load_locids(loc_dirpath=os.path.join(mod_dirpath, 'localisation'))
    logging.info(f"Localisation identifiers count: {len(locids)}")
    stats = SearchStats(locids=locids)
    # Search all localisation usage
    subjfiles = _load_subjfiles(mod_dirpath=mod_dirpath, excluded_subdirs=excluded_subdirs)
    logging.info(f"Search files count: {len(subjfiles)}")
    logging.info(f"Searching for localisations...")
    for subjfile in subjfiles:
        for locid, line_nr, indents in subjfile.search_locids(locids=locids):
            stats.add(subjname=subjfile.subjname, category=subjfile.category, line_nr=line_nr, indents=indents, locid=locid)
    return stats


def write_stats(statsdir: str, stats: 'SearchStats'):
    os.makedirs(statsdir, exist_ok=True)
    with open(f'{statsdir}/locfile_stats.tsv', 'w', encoding='utf-8') as fh:
        stats.write_sources_stats(fh=fh)
    with open(f'{statsdir}/subjfile_data.json', 'w', encoding='utf-8') as fh:
        stats.write_subj_data(fh=fh)


def write_output(outdir: str, stats: 'SearchStats'):
    os.makedirs(outdir, exist_ok=True)
    with open(f'{outdir}/xxx_new_unsorted_l_english.yml', 'w', encoding='utf-8') as fh:
        fh.write("l_english:\n # Dump your new localisations here, they will be automatically sorted next time the localisation search is run!\n")
    with open(f'{outdir}/xxx_unused_l_english.yml', 'w', encoding='utf-8') as fh:
        stats.write_unused_locs(fh=fh)
    stats.write_used_locs(outdir=outdir)


def main(from_stats=False):
    log_setup(logs_dir=LOGS_DIR)
    logging.info(f"Excluded subdirs: {EXCLUDED_SUBDIRS}")
    if from_stats:
        subjfile_data_filepath = f"{STATSDIR}/subjfile_data.json"
        stats = get_stats(mod_dirpath=str(MOD_DIR), subjfile_data_filepath=subjfile_data_filepath)
    else:
        stats = search_stats(mod_dirpath=str(MOD_DIR), excluded_subdirs=EXCLUDED_SUBDIRS)
    logging.info(f"Found: {stats.found}/{stats.total} ({stats.found/stats.total:.0%})")
    logging.info(f"Missing: {stats.missing}/{stats.total} ({stats.missing/stats.total:.0%})")
    write_stats(statsdir=STATSDIR, stats=stats)
    write_output(outdir=OUTDIR, stats=stats)
    logging.info("Done!")


if __name__ == '__main__':
    main(from_stats=False)


#
#
# END OF FILE
