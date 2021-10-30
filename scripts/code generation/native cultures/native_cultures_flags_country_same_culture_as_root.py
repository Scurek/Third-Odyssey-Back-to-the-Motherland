from cultures_by_group import *
from jinja2 import Template, Environment

output_file = "output_country_same_culture_as_root.txt"

template = Template('''{%- for cultures in culture_groups.values() %}
{%- for culture in cultures %}
OR = { AND = { primary_culture = {{ culture }} ROOT = { has_province_flag = nat_original_culture_{{ culture }} } } }
{%- endfor %}
{%- endfor %}
''')

# cultures = []
# for culture_group in culture_groups.values():
#     cultures.extend(culture_group)

f = open(output_file, "w")
f.write(template.render(culture_groups=culture_groups))
f.close()
