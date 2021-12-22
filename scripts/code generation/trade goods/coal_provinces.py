import os
import re

output = "output_coal.txt"
eu4_provinces_path = "C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis IV\history\provinces"

o = open(output, "w")
for filename in os.listdir(eu4_provinces_path):
    with open(os.path.join(eu4_provinces_path, filename)) as f:
        lines = f.readlines()
        for line in lines:
            if re.match("^[^#]*coal.*$", line):
                province_id = filename.split("-")[0]
                o.write("province_id = " + str(province_id) + "\n")
o.close()
