"""
Scrape the localisation files and search if and where they're used, based on pure regex text search.

Author: lichtkang
"""

import os
import sys
import pathlib

if sys.version_info < (3, 9):
    sys.exit("Needs Python 3.9 or higher")

import re
import typing as t


# -- Globals --

# Directory of the mod. Change this if needed. Assuming certain relative positions of script to files.
MOD_DIR = pathlib.Path(__file__).absolute().parent.parent.joinpath('deploy')
# Subdirectories within the mod to exclude from search
EXCLUDED_SUBDIRS = [
    'localisation',  # Of course, if we don't exclude localisation, we'll find all!
    #'customizable_localisation', 'dlc_recommendations', 'gfx', 'history', 'interface', 'map', 'sound' 
]


# -- Public Methods --

def get_search_files(mod_dirpath: str, excluded_subdirs: list[str]) -> list[str]:
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


def get_localisation_files(mod_dirpath: str):
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

def get_loc_ids_patterns(filepaths: list[str]) -> dict[str, t.Pattern]:
    """Load localisation identifiers and search patterns from a set of filepaths."""
    loc_ids_patterns = dict()
    for filepath in filepaths:
        with open(filepath, 'r') as fh:
            fh.readline()  # Skip first line, which specifies language
            for line in fh:
                if not line.strip():
                    continue
                try:
                    identifier, _ = line.strip().split(':', 1)
                except ValueError:
                    continue  # Too few variables to unpack (corrupt), skip
                else:
                    loc_ids_patterns[identifier] = re.compile(r"\b{identifier}\b")
    return loc_ids_patterns


def scan_file_loc_ids(filepath: str, loc_ids_patterns: dict[str, t.Pattern]) -> list[str]:
    """Scan a file for the presence of localisation identifiers."""
    with open(filepath, 'r') as fh:
        content = fh.read()  # Assume we can load whole files in memory without issues. Should speed up search compared to line-by-line.
    found = []
    for loc_id, pattern in loc_ids_patterns.items():
        if loc_id in content:  # Seems good enough for now
        #if pattern.search(content) is not None:
            found.append(loc_id)
    return found


def iter_scan_files_loc_ids(filepaths: list[str], loc_ids_patterns: dict[str, t.Pattern]) -> t.Iterator[tuple[str, list[str]]]:
    """Iteratively scan multiple files for the presence of localisation identifiers"""
    for filepath in filepaths:
        yield filepath, scan_file_loc_ids(filepath=filepath, loc_ids_patterns=loc_ids_patterns)


# -- Run as Script --

def main():
    print(f"Mod dir: {MOD_DIR}")
    loc_filepaths = get_localisation_files(mod_dirpath=MOD_DIR)
    print(f"Localisation files: {len(loc_filepaths)}")
    loc_ids_patterns = get_loc_ids_patterns(filepaths=loc_filepaths)
    print(f"Localisation identifiers: {len(loc_ids_patterns)}")
    search_filepaths = get_search_files(mod_dirpath=MOD_DIR, excluded_subdirs=EXCLUDED_SUBDIRS)
    print(f"Search files: {len(search_filepaths)}")
    all_found = set()
    for filepath, results in iter_scan_files_loc_ids(filepaths=search_filepaths, loc_ids_patterns=loc_ids_patterns):
        all_found.update(results)
    not_found = set(loc_ids_patterns.keys()).difference(all_found)
    print(f"Found: {len(all_found)}")
    print(f"Missing: {len(not_found)}")


if __name__ == '__main__':
    main()


#
#
# END OF FILE
