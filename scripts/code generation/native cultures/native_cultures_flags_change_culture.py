from cultures_by_group import *
from jinja2 import Template, Environment

output_file = "output_change_culture.txt"

template = Template('''{%- for culture in cultures %}
{%- if loop.first -%}
if = {
{%- else %}
else_if = {
{%- endif %}
    limit = { has_province_flag = nat_original_culture_{{ culture }} }
    change_culture = {{ culture }}
}
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render(cultures=cultures))
f.close()
