from exarchs import exarchs
from shutil import copy2
from os import path

province_name_directory = "../../../deploy/common/province_names"
original_file = "byzantine.txt"
other_cultures = ["spartakian_group"]

exarch_tags = []
for exarch in exarchs:
    exarch_tags.append(exarch['tag'])

for tag in exarch_tags + other_cultures:
    copy2(path.join(province_name_directory, original_file), path.join(province_name_directory, tag + ".txt"))
