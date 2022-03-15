from cultures_by_group import *
from jinja2 import Template, Environment

output_file = "output_same_culture_group_province.txt"

template = Template('''\tOR = {
{%- for culture_group, cultures in culture_groups.items() %}
\t\tAND = {
\t\t\tculture_group = {{ culture_group }}
\t\t\t$PROVINCE_SCOPE$ = {
\t\t\t\tOR = {
{%- for culture in cultures %}
\t\t\t\t\thas_province_flag = nat_original_culture_{{ culture }}
{%- endfor %}
\t\t\t\t}
\t\t\t}
\t\t}
{%- endfor %}
\t}
''')

# cultures = []
# for culture_group in culture_groups.values():
#     cultures.extend(culture_group)

f = open(output_file, "w")
f.write(template.render(culture_groups=culture_groups))
f.close()
