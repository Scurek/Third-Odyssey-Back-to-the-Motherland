"""
Scrape the localisation files and search if and where they're used, based on pure regex text search.

Author: lichtkang
"""

import os
import sys
import json
import pathlib
import logging
import logging.handlers
import datetime
import collections

if sys.version_info < (3, 9):
    sys.exit("Needs Python 3.9 or higher")

import re
import typing as t


# -- Globals --

# Directory of the mod. Change this if needed. Assuming certain relative positions of script to files.
MOD_DIR = pathlib.Path(__file__).absolute().parent.parent.parent.joinpath('deploy')
# Subdirectories within the mod to exclude from search
EXCLUDED_SUBDIRS = [
    'localisation',  # Of course, if we don't exclude localisation, we'll find all!
    'gfx',
    'history',
    'interface',
    'sound'
]


# -- Logging --

def log_setup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H_%M_%S")
    log_handler = logging.FileHandler(f'{timestamp}.log', mode='w', encoding='utf-8')
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%b %d %H:%M:%S'
    )
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)


log_setup()


# -- Public Methods --

def get_search_files(mod_dirpath: os.PathLike, excluded_subdirs: list[str]) -> list[str]:
    """Get the files which should be searched for localisations."""
    filepaths = []
    excluded_subdirs = {os.path.join(mod_dirpath, subdir.lower()) for subdir in excluded_subdirs}
    for root, dirs, files in os.walk(mod_dirpath):
        if root in excluded_subdirs:
            continue
        filepaths.extend([
            os.path.join(root, filename)
            for filename in files
            if filename.endswith('.txt')
        ])
    return filepaths


def get_localisation_files(mod_dirpath: os.PathLike):
    """Get all files containing localisation."""
    locs_path = os.path.join(mod_dirpath, 'localisation')
    return [
        os.path.join(locs_path, filename)
        for filename in os.listdir(locs_path)
        if (
            filename.endswith('l_english.yml') 
            and os.path.isfile(os.path.join(locs_path, filename))
        )
    ]


def get_loc_ids_patterns(filepaths: list[str]) -> tuple[dict[str, set[str]], dict[str, t.Pattern], dict[str, str]]:
    """Load localisation identifiers and search patterns from a set of filepaths. Both as mapping to patterns, and in groups by filepath."""
    loc_ids_patterns = dict()
    loc_ids_text = dict()
    locfile2ids = collections.defaultdict(set)
    for filepath in filepaths:
        with open(filepath, 'r') as fh:
            fh.readline()  # Skip first line, which specifies language
            for line_nr, line in enumerate(fh, start=2):
                if not line.strip() or line.strip().startswith('#'):
                    continue
                try:
                    identifier, text = line.strip().split(':0', 1)
                except ValueError:
                    # Too few variables to unpack (corrupt), skip
                    logging.warning(f"Corruption in localisation file '{os.path.basename(filepath)}', line {line_nr}")
                    continue
                else:
                    identifier, text = identifier.strip(), text.strip()
                    locfile2ids[filepath].add(identifier)
                    if identifier in loc_ids_text:
                        logging.warning(f"Duplicate localisation identifier: {identifier}")
                    else:
                        loc_ids_text[identifier] = text
                        loc_ids_patterns[identifier] = re.compile(rf"^[^#]*\b{identifier}\b.*$", re.MULTILINE)
    return locfile2ids, loc_ids_patterns, loc_ids_text


def scan_file_loc_ids(filepath: str, loc_ids_patterns: dict[str, t.Pattern]) -> set[str]:
    """Scan a file for the presence of localisation identifiers."""
    with open(filepath, 'r') as fh:
        content = fh.read()  # Assume we can load whole files in memory without issues. Should speed up search compared to line-by-line.
    found = set()
    for loc_id, pattern in loc_ids_patterns.items():
        if loc_id in content:  # Quick first check
            for line in content.splitlines():
                if loc_id in line and pattern.search(line) is not None:
                    found.add(loc_id)
                    break
    return found


def iter_scan_files_loc_ids(filepaths: list[str], loc_ids_patterns: dict[str, t.Pattern]) -> t.Iterator[tuple[str, set[str]]]:
    """Iteratively scan multiple files for the presence of localisation identifiers"""
    for filepath in filepaths:
        yield filepath, scan_file_loc_ids(filepath=filepath, loc_ids_patterns=loc_ids_patterns)


# -- Run as Script --

def get_data(mod_dir: os.PathLike, excluded_subdirs: list[str]) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, str], set[str], set[str]]:
    loc_filepaths = get_localisation_files(mod_dirpath=mod_dir)
    logging.info(f"Localisation files count: {len(loc_filepaths)}")
    locfile2ids, loc_ids_patterns, loc_ids_text = get_loc_ids_patterns(filepaths=loc_filepaths)
    logging.info(f"Localisation identifiers count: {len(loc_ids_patterns)}")
    search_filepaths = get_search_files(mod_dirpath=mod_dir, excluded_subdirs=excluded_subdirs)
    logging.info(f"Search files count: {len(search_filepaths)}")
    # Search all localisation usage
    subjfile2found = dict()
    all_found = set()
    for filepath, results in iter_scan_files_loc_ids(filepaths=search_filepaths, loc_ids_patterns=loc_ids_patterns):
        all_found.update(results)
        if results:
            subjfile2found[filepath] = results
    not_found = set(loc_ids_patterns.keys()).difference(all_found)
    return locfile2ids, subjfile2found, loc_ids_text, all_found, not_found


def write_locfile_stats(filepath: str, locfile2ids: dict[str, set[str]], all_found: set[str]):
    locfile_stats = []
    for locfile, all_locs in locfile2ids.items():
        found_locs = all_locs.intersection(all_found)
        locfile_stats.append((
            os.path.basename(locfile),
            len(found_locs)/len(all_locs),  # Usage
            len(all_locs),  # Total identifiers
        ))
    locfile_stats.sort(key=lambda x: x[1])  # Sort from lowest to highest usage
    with open(filepath, 'w', encoding='utf-8') as out_fh:
        out_fh.write('Filename\tTotal\tUsage\n')
        for filename, perc_used, total in locfile_stats:
            out_fh.write(f"{filename}\t{perc_used:.0%}\t{total}\n")


def write_subjfile_data(filepath: str, subjfile2found: dict[str, set[str]], ):
    with open(filepath, 'w', encoding='utf-8') as out_fh:
        json.dump(
            obj={
                filepath: sorted(loc_ids)
                for filepath, loc_ids in subjfile2found.items()
            },
            fp=out_fh,
            indent='\t',
        )


def write_unused_locs(filepath: str, not_found: set[str], loc_ids_text: dict[str, str]):
    with open(filepath, 'w', encoding='utf-8') as out_fh:
        out_fh.write('l_english:\n')
        for loc_id in sorted(not_found):
            text = loc_ids_text[loc_id]
            out_fh.write(f' {loc_id}:0 {text}\n')


def main():
    logging.info(f"Mod dir: {MOD_DIR}")
    logging.info(f"Excluded subdirs: {EXCLUDED_SUBDIRS}")
    locfile2ids, subjfile2found, loc_ids_text, all_found, not_found = get_data(mod_dir=MOD_DIR, excluded_subdirs=EXCLUDED_SUBDIRS)
    logging.info(f"Found: {len(all_found)}/{(len(all_found)+len(not_found))} ({len(all_found)/(len(all_found)+len(not_found)):.0%})")
    write_locfile_stats(filepath='locfile_stats.tsv', locfile2ids=locfile2ids, all_found=all_found)
    write_subjfile_data(filepath='subjfile_data.json', subjfile2found=subjfile2found)
    write_unused_locs(filepath='unused.yml', not_found=not_found, loc_ids_text=loc_ids_text)


if __name__ == '__main__':
    main()


#
#
# END OF FILE
