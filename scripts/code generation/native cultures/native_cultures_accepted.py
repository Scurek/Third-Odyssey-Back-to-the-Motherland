from cultures import *
from jinja2 import Template, Environment

output_file = "output_accepted.txt"

template = Template('''OR = {
{%- for culture in cultures %}  
    accepted_culture = {{ culture }}
{%- endfor %}
}
''')

# cultures = []
# for culture_group in culture_groups.values():
#     cultures.extend(culture_group)

f = open(output_file, "w")
f.write(template.render(cultures=cultures))
f.close()
