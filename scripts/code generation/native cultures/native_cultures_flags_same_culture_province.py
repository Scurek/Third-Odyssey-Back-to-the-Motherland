from cultures_by_group import *
from jinja2 import Template, Environment

output_file = "output_same_culture_province.txt"

template = Template('''\tOR = {
{%- for culture in cultures %}
\t\tAND = { culture = {{ culture }} $PROVINCE_SCOPE$ = { has_province_flag = nat_original_culture_{{ culture }} } }
{%- endfor %}
    }
''')

# cultures = []
# for culture_group in culture_groups.values():
#     cultures.extend(culture_group)

f = open(output_file, "w")
f.write(template.render(cultures=cultures))
f.close()
