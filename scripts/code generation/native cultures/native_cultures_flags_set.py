from string import Template
from cultures_by_group import *

output_file = "output_flags_set.txt"

template_if = Template('''\t$if = { limit = { culture = $culture } set_province_flag = nat_original_culture_$culture }
''')

f = open(output_file, "w")
output = template_if.substitute({'if': 'if', 'culture': cultures[0]})
f.write(output)
for culture in cultures[1:]:
    output = template_if.substitute({'if': 'else_if', 'culture': culture})
    f.write(output)
f.close()
