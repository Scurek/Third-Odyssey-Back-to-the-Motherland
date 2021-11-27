from jinja2 import Template, Environment

output_file = "output.txt"

template = Template('''{%- for i in range(50, 0, -1) %}
{%- if loop.first -%}
if = {
{%- else %}
else_if = {
{%- endif %}
    limit = { check_variable = { which = $VARIABLE_NAME$ value = {{ i }} } }
    add_province_modifier = { name = $MODIFIER$ duration = {{ i * 365 }} }
}
{%- endfor %}
''')

# cultures = []
# for culture_group in culture_groups.values():
#     cultures.extend(culture_group)

f = open(output_file, "w")
f.write(template.render())
f.close()
