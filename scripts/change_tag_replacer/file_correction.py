import os
import re
import chardet
from defines import *

CHANGE_TAG = r"change_tag *= *\w{3}"
CHANGE_TAG_EFFECT = r"[^\S\r\n]*[^a-zA-z-_]on_change_tag_effect[^\S\r\n]*=[^\S\r\n]*yes[^\S\r\n]*\n?"
def file_correction():
    for foldername, subfolders, filenames in os.walk(MOD_PATH, topdown=True):
        if os.path.basename(foldername) == "deploy":
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
                    with open(file_path, 'r+', encoding=encoding['encoding']) as file:
                        file_contents = file.read()
                        relative_file_path = os.path.relpath(file_path, MOD_PATH)
                        if re.search(CHANGE_TAG, file_contents):
                            print(f"Correcting change_tag in {relative_file_path}")
                            file.seek(0)
                            file.write(re.sub(r'change_tag *= *(\w{3})', r'to_change_tag = { TAG = \1 }',
                                              file_contents))
                            file.truncate()
                    with open(file_path, 'r+', encoding=encoding['encoding']) as file:
                        file_contents = file.read()
                        relative_file_path = os.path.relpath(file_path, MOD_PATH)
                        if re.search(CHANGE_TAG_EFFECT, file_contents):
                            print(f"Removing on_change_tag_effect in {relative_file_path}")
                            file.seek(0)
                            file.write(re.sub(CHANGE_TAG_EFFECT, "", file_contents))
                            file.truncate()

                except Exception as e:
                    print(f"Error: {e}")


file_correction()