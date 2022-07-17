from exarch_tags import tags
from shutil import copy2
from os import path

province_name_directory = "../../../deploy/common/province_names"
original_file = "byzantine.txt"
other_cultures = ["spartakian_group"]

for tag in tags + other_cultures:
    copy2(path.join(province_name_directory, original_file), path.join(province_name_directory, tag + ".txt"))
