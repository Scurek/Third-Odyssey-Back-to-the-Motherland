from string import Template
from cultures import *

output_file = "output_restore_culture.txt"

template_if = Template('''$if = {
    limit = { has_province_flag = nat_original_culture_$culture }
    change_culture = $culture change_religion = totemism
}
''')

f = open(output_file, "w")
output = template_if.substitute({'if': 'if', 'culture': cultures[0]})
f.write(output)
for culture in cultures[1:]:
    output = template_if.substitute({'if': 'else_if', 'culture': culture})
    f.write(output)
f.close()
