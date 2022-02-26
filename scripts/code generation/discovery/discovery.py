from jinja2 import Template, Environment

output_file = "output.txt"
undiscover_file = "output_undiscover.txt"

base_flag = "to_byz_flight_discovery_path"

province_sequence = [1566, 1567, 1580, 1583, 1575, 1574, 1571, 1501, 5377] # 367

template = Template('''{%- for prov_id in province_sequence %}
{%- if loop.first -%}
if = {
{%- else %}
else_if = {
{%- endif %}
    limit = {
        has_country_flag = {{ base_flag }}_{{ loop.index }}
    }
    discover_province = {{ prov_id }}
    clr_country_flag = {{ base_flag }}_{{ loop.index }}
    {% if not loop.last -%}
        set_country_flag = {{ base_flag }}_{{ loop.index + 1 }}
    {%- endif %}
}
{%- endfor %}
''')

template_undiscover = Template('''{%- for prov_id in province_sequence %}
    undiscover_province = {{ prov_id }}
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render(province_sequence=province_sequence, base_flag=base_flag))
f.close()

f = open(undiscover_file, "w")
f.write(template_undiscover.render(province_sequence=province_sequence))
f.close()