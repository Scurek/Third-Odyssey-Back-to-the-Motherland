from cultures_by_group import *
from jinja2 import Template, Environment

output_file = "output_same_culture_group.txt"

template = Template('''{%- for culture_group, cultures in culture_groups.items() %}
{%- if loop.first -%}
if = {
{%- else %}
else_if = {
{%- endif %}
    limit = {
        owner = { culture_group = {{ culture_group }} }
    }
    OR = {
        {%- for culture in cultures %}
        has_province_flag = nat_original_culture_{{ culture }}
        {%- endfor %}
    }
}
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render(culture_groups=culture_groups))
f.close()
