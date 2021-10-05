from jinja2 import Template, Environment

output_file = "output_save.txt"

reforms = [
    "to_native_reform_egalitarian",
    "to_native_reform_stratified",
    "to_native_reform_theocracy",
    "to_native_reform_nomadic_raiders",
    "to_council_of_cities_reform",
    "to_native_parliament_reform",
    "to_grand_chiefdom_reform",
    "to_native_kingdom_reform"
]

template = Template('''{%- for reform in reforms -%}
    {%- if loop.first %}
    if = {
    {%- else %}
    else_if = {
    {%- endif %}
        limit = {
            has_reform = {{ reform }}
        }
        set_country_flag = to_had_native_reform_{{ reform }}
    }
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render(reforms=reforms))
f.close()
