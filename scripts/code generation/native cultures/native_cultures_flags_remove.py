from string import Template
from cultures_by_group import *

output_file = "output_remove_culture_flags.txt"

template = Template('''clr_province_flag = nat_original_culture_$culture
''')

f = open(output_file, "w")
for culture_group in culture_groups.values():
    for culture in culture_group:
        output = template.substitute({'culture': culture})
        f.write(output)
f.close()
