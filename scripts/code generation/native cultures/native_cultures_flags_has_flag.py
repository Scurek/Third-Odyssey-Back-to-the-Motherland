from cultures_by_group import *
from jinja2 import Template, Environment

output_file = "output_has_flag.txt"

template = Template('''OR = {
{%- for culture in cultures %}
    has_province_flag = nat_original_culture_{{ culture }}
{%- endfor %}
}
''')

f = open(output_file, "w")
f.write(template.render(cultures=cultures))
f.close()
