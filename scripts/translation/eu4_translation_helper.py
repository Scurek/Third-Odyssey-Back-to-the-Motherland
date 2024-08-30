#!/usr/bin/env python3
"""
A helper for EU4 translations.

Author: lichtkang
"""

import sys

if sys.version_info < (3, 9):
    # Not checked, but safe assumption
    sys.exit("Needs Python 3.9 or higher")

import argparse
import collections
import csv
import dataclasses
import datetime
import json
import logging
import os
import pathlib
import re
import typing as t

# -- Localisation parsing --


@dataclasses.dataclass
class LocLine:
    identifier: str
    text: str


@dataclasses.dataclass
class LocFile:
    sourcefile: pathlib.Path
    language: str
    lines: list[LocLine]


LocId: t.TypeAlias = str
LangId: t.TypeAlias = str
Text: t.TypeAlias = str


@dataclasses.dataclass
class LocalisationData:
    languages: set[LangId] = dataclasses.field(default_factory=set)
    entries: dict[LocId, dict[LangId, Text]] = dataclasses.field(default_factory=lambda: collections.defaultdict(dict))


_LOC_LANG_RE = re.compile(r"^l_([a-z]+):$")
_LOC_SEPARATOR_RE = re.compile(r":[0-9]")


def _load_loc_from_file(filepath: pathlib.Path) -> LocFile | None:
    lines = []
    with open(filepath, "r", encoding="utf-8-sig") as fh:
        # Get the language
        language_raw = fh.readline().strip()
        language_match = _LOC_LANG_RE.match(language_raw)
        if not language_match:
            logging.warning(f"Could not find language from file {filepath.name!r}")
            return
        language = language_match.group(1)
        # Parse lines
        for line_nr, line in enumerate(fh, start=2):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                identifier, text = _LOC_SEPARATOR_RE.split(line, maxsplit=1)
            except ValueError:
                logging.warning(f"Invalid entry in localisation file {filepath.name!r}, line {line_nr}")
                continue
            else:
                text = text.strip().removeprefix('"').removesuffix('"').replace('\\"', '"')
                lines.append(
                    LocLine(
                        identifier=identifier.strip(),
                        text=text.strip(),
                    )
                )
    return LocFile(sourcefile=filepath, language=language, lines=lines)


def _merge_localisations(locfiles: list[LocFile]) -> LocalisationData:
    locdata = LocalisationData()
    for locfile in locfiles:
        locdata.languages.add(locfile.language)
        for locline in locfile.lines:
            if locfile.language in locdata.entries[locline.identifier]:
                logging.warning(
                    f"Skipping duplicate definition of {locline.identifier!r} in language {locfile.language!r}"
                )
                continue
            locdata.entries[locline.identifier][locfile.language] = locline.text
    return locdata


def parse_localisation_from_locfiles(dirpath: pathlib.Path, exclude_patterns: list[str]) -> LocalisationData:
    locfiles = []
    exclude_patterns_re = [re.compile(raw) for raw in exclude_patterns]
    for filepath in dirpath.iterdir():
        if not filepath.is_file():
            continue
        if any(pattern.match(str(filepath)) for pattern in exclude_patterns_re):
            continue
        locfile = _load_loc_from_file(filepath=filepath)
        if locfile is not None:
            locfiles.append(locfile)
    return _merge_localisations(locfiles=locfiles)


def parse_localisation_from_tsv(filepath: pathlib.Path) -> LocalisationData:
    locdata = LocalisationData()
    with open(filepath, "r") as fh:
        reader = csv.DictReader(
            fh,
            delimiter="\t",
        )
        locdata.languages.update(name for name in reader.fieldnames if name != "identifier")
        for entry in reader:
            identifier = entry["identifier"]
            for language in locdata.languages:
                locdata.entries[identifier][language] = entry[language]
    return locdata


def write_localisation_to_locfiles(loc_dir: pathlib.Path, locdata: LocalisationData, reference_language: str):
    """Write language localisations to files, except the reference language"""
    output_languages = sorted(lang for lang in locdata.languages if lang != reference_language)
    logging.info(
        f"Writing localisation files for languages: {','.join(output_languages)} "
        f"(ignoring reference language {reference_language!r})"
    )
    for lang in output_languages:
        filepath = loc_dir / f"all_l_{lang}.yml"
        with open(filepath, "w") as fh:
            fh.write(f"l_{lang}:\n")
            for identifier, lang_text_map in locdata.entries.items():
                if text := lang_text_map[lang]:
                    text = text.replace('"', '\\"')
                    fh.write(f' {identifier}:0 "{text}"\n')


def write_localisation_to_tsv(outpath: pathlib.Path, locdata: LocalisationData, reference_language: str):
    output_languages = sorted(lang for lang in locdata.languages if lang != reference_language)
    with open(outpath, "w") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["identifier", reference_language, *output_languages],
            delimiter="\t",
        )
        writer.writeheader()
        for identifier, lang_text_map in locdata.entries.items():
            entry_dict = {"identifier": identifier}
            entry_dict.update(lang_text_map)
            writer.writerow(entry_dict)


# -- Execute --


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert EU4's YAML localisation files to one TSV file for translation, or vice-versa. \n"
            "The TSV file can be edited in Excel or similar programs, but take care to save as TSV and not an excel-specific format! \n"
            "Without arguments, loads the localisation to a TSV file. Use the 'flush' flag to write back and backup the TSV (prefixed by 'previous_')."
            "Quirks specific for translation: \n"
            "    - Will not overwrite existing TSV files, use 'flush' to flush changes to the localisation files first. \n"
            "    - Only languages other than the reference language are written to localisation files. \n"
        ),
        epilog="Author: lichtkang",
    )
    parser.add_argument("--flush", action="store_true", help="Flush translations to localisation files")
    arguments = parser.parse_args()
    return arguments


def _load_to_tsv(
    loc_dir: pathlib.Path,
    tsv_filepath: pathlib.Path,
    reference_language: str,
    exclude_patterns: list[str],
):
    """Load localisation to TSV file"""
    if tsv_filepath.exists():
        raise RuntimeError(
            f"The TSV file already exists, use the 'flush' flag to flush pending changes "
            f"to the localisation files first. Filepath: {str(tsv_filepath)!r}"
        )
    locdata = parse_localisation_from_locfiles(dirpath=loc_dir, exclude_patterns=exclude_patterns)
    write_localisation_to_tsv(outpath=tsv_filepath, locdata=locdata, reference_language=reference_language)


def _flush_to_localisation(
    loc_dir: pathlib.Path,
    tsv_filepath: pathlib.Path,
    reference_language: str,
):
    """Write TSV file to localisation and rename it"""
    locdata = parse_localisation_from_tsv(filepath=tsv_filepath)
    write_localisation_to_locfiles(
        loc_dir=loc_dir,
        locdata=locdata,
        reference_language=reference_language,
    )
    backup_tsv_filepath = tsv_filepath.parent / f"previous_{tsv_filepath.name}"
    tsv_filepath.rename(backup_tsv_filepath)


def main():
    arguments = _parse_arguments()
    # Load configuration
    parent_dir = pathlib.Path(__file__).parent
    try:
        with open(parent_dir / "config.json", "r") as fh:
            config = json.load(fh)
    except IOError:
        raise RuntimeError(
            "Could not find the required `config.json`. Please ensure it is present in the same directory as this script."
        )
    loc_dir = pathlib.Path(config["localisation_directory"])
    tsv_filepath = pathlib.Path(config["tsv_filepath"])
    reference_language = config["reference_language"]
    exclude_patterns = config["exclude_patterns"]
    # Execute
    try:
        if arguments.flush:
            _flush_to_localisation(
                loc_dir=loc_dir,
                tsv_filepath=tsv_filepath,
                reference_language=reference_language,
            )
        else:
            _load_to_tsv(
                loc_dir=loc_dir,
                tsv_filepath=tsv_filepath,
                reference_language=reference_language,
                exclude_patterns=exclude_patterns,
            )
    except RuntimeError as e:
        print(e)
        sys.exit(1)
    logging.info("Done!")


if __name__ == "__main__":
    main()
