from jinja2 import Template, Environment

output_file = "output_restore_council_stats.txt"


template = Template('''{%- for i in range(6, -1 , -1) %}
{%- if loop.first -%}
if = {
{%- else %}
else_if = {
{%- endif %}
    limit = { check_variable = { which = to_native_council_adm value = {{ i }} } }
    {% for j in range(6, -1 , -1) %}
    {%- if loop.first -%}
    if = {
    {%- else %}
    else_if = {
    {%- endif %}
        limit = { check_variable = { which = to_native_council_dip value = {{ j }} } }
        {% for k in range(6, -1 , -1) %}
        {%- if loop.first -%}
        if = {
        {%- else %}
        else_if = {
        {%- endif %}
            limit = { check_variable = { which = to_native_council_mil value = {{ k }} } }
            generate_council_ruler_with_skills = { ADM = {{ i }} DIP = {{ j }} MIL = {{ k }} }
        }
        {%- endfor %}
    }
    {%- endfor %}
}
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render())
f.close()