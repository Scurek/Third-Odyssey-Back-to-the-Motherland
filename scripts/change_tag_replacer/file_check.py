import os
import re
import chardet
import shutil
from defines import *

CHANGE_TAG = r"change_tag ?= ?[a-zA-Z]{3}"

# Function to iterate over text files in a folder and its subfolders
def file_check(folder_path, copy=False):
    for foldername, subfolders, filenames in os.walk(folder_path, topdown=True):
        if os.path.basename(foldername) == "Europa Universalis IV":
            subfolders[:] = [d for d in subfolders if d in INCLUDED_FOLDERS]
            continue
        elif os.path.basename(foldername) == "common":
            subfolders[:] = [d for d in subfolders if d not in EXCLUDED_FOLDERS_COMMON]

        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'rb') as file:
                    encoding = chardet.detect(file.read())
                try:
                    with open(file_path, 'r', encoding=encoding['encoding']) as file:
                        file_contents = file.read()
                        if re.search(CHANGE_TAG, file_contents):
                            relative_file_path = os.path.relpath(file_path, EU4_PATH)
                            mod_file_path = os.path.join(MOD_PATH, relative_file_path)
                            if not os.path.exists(mod_file_path):
                                print(f"Mod missing {relative_file_path}")
                                if copy:
                                    directory = os.path.dirname(mod_file_path)
                                    if not os.path.exists(directory):
                                        os.makedirs(directory)
                                    shutil.copy2(file_path, mod_file_path)

                except Exception as e:
                    print(f"Error: {e}")


file_check(EU4_PATH, True)
