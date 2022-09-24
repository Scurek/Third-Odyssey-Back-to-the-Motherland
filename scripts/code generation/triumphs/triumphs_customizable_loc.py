import os

from jinja2 import Template, Environment
output_file = "o_customizable_loc.txt"
output_file_loc = "o_loc.txt"

jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])

class Region:
    def __init__(self, region, provinces, name, province, cities=None, region_format="Region", order=0):
        self.region = region
        self.provinces = provinces
        self.name = name
        self.province = province
        self.region_format = region_format
        self.cities = cities
        self.order = order


regions = [
    Region("anatolia_region", 30, "Anatolia", 316, [318, 317]),  # Total 48
    Region("mashriq_region", 20, "Syria", 379, [2313]),  # Total 30
    Region("egypt_region", 20, "Aigyptos", 358, [358]),  # Total 29
    Region("maghreb_region", 30, "Afrika", 343, [341]),  # Total 63
    Region("iberia_region", 40, "Spania", 217, [225, 213]),  # Total 62 | 218, 220
    Region("italy_region", 40, "Italia", 118, [118, 104, 114]),  # Total 57
    Region("france_region", 40, "Frankia", 183, [183, 203]),  # Total 66
    Region("south_german_region", 40, "Ano Germania", 134, [134, 1868], region_format="Reg."),  # Total 64
    Region("british_isles_region", 30, "Anglia", 236, [236]),  # Total 56
    Region("carpathia_region", 15, "Pannonia", 153, [153],
           order=1),  # Total 31
    Region("low_countries_region", 15, "Kato Germania", 92, [1744],
           region_format="Reg.", order=1),  # Total 22
    # Balkans Total 57
]

variants = max(regions, key=lambda x: x.order).order

template = Template('''{%- for region in regions %}
defined_text = {
	name = Get_{{ region.region }}_TriumphStatus
	random = no
	text = {
		localisation_key = to_y_icon_tt
		trigger = {
			to_has_completed_triumph = { REGION = {{ region.region }} }
			{% if region.cities is not none %}{% for city in region.cities -%}
			owns_or_subject_of = {{ city }}
			{% endfor %}{% endif %}
		}
	}

	text = {
		localisation_key = to_x_icon_tt
	}
}

defined_text = {
	name = Get_{{ region.region }}_TriumphProgress
	random = no
	text = {
		localisation_key = to_nat_yellow_zero_tt
		trigger = {
		    NOT = {
		        check_variable = {
		            which = to_{{ region.region }}_provinces
			        value = 1
		        }
		    }
		}
	}

	text = {
		localisation_key = to_{{ region.region }}_triumph_progress_tt
	}
}
{%- endfor %}
''')

template_loc = Template(
    "{% for region in regions %}"
    " to_{{ region.region }}_triumph_check_tt:0 \""
    "[Get_{{ region.region }}_TriumphStatus][{{ region.province }}.GetRegionName] "
    # "{{ region.region_format }} (§YTriumph for {{ region.name }}§!):\\n§Y{{ region.provinces }}§! "
    "{{ region.region_format }}:\\n§Y{{ region.provinces }}§! "
    "provinces (current: [Get_{{ region.region }}_TriumphProgress]) owned by you or your subjects."
    "{% if region.cities is not none %}"
    "\\n"
    "{% for city in region.cities %}"
    "{% if loop.last and not loop.first %}"
    " and "
    "{% elif not loop.first %}"
    ", "
    "{% endif %}"
    "§Y[{{ city }}.GetName]§!"
    "{% endfor %}"
    " owned by you or your subjects."
    "{% endif %}"
    "\"\n"
    "{% endfor %}"
)

template_loc_v2 = jinja_env.from_string(
    "{% for i in range(variants) %}"
    "to_triumphs_completed_count_var_{{ i }}_tt:0 \""
    " Triumphs Completed:\\n§gEach Triumph requires direct or subject ownership of one or more specific "
    "cities and certain number of provinces within a region.§!"
    "{% for region in regions %}"
    "{% if i < region.order %}{% continue %}{% endif %}"
    "\\n"
    "   [Get_{{ region.region }}_TriumphStatus][{{ region.province }}.GetRegionName] "
    "{{ region.region_format }}"
    "{% if region.cities is not none %}"
    " ("
    "{% for city in region.cities %}"
    "{% if loop.last and not loop.first %}"
    " and "
    "{% elif not loop.first %}"
    ", "
    "{% endif %}"
    "§Y[{{ city }}.GetName]§!"
    "{% endfor %}"
    ")"
    "{% endif %}"
    ":\\n"
    "§Y{{ region.provinces }}§! "
    "provinces (current: [Get_{{ region.region }}_TriumphProgress]) owned by you or your subjects."
    "{% endfor %}"
    "\"\n\n"
    "{% endfor %}"
    )

template_loc_v2_all = jinja_env.from_string(
    "to_triumphs_completed_all_tt:0 \""
    "All Triumphs have been completed:\\n§gEach Triumph requires direct or subject ownership of one or "
    "more specific cities and certain number of provinces within a region.§!"
    "{% for region in regions %}"
    "\\n"
    "   [Get_{{ region.region }}_TriumphStatus][{{ region.province }}.GetRegionName] "
    "{{ region.region_format }}"
    "{% if region.cities is not none %}"
    " ("
    "{% for city in region.cities %}"
    "{% if loop.last and not loop.first %}"
    " and "
    "{% elif not loop.first %}"
    ", "
    "{% endif %}"
    "§Y[{{ city }}.GetName]§!"
    "{% endfor %}"
    ")"
    "{% endif %}"
    ":\\n"
    "§Y{{ region.provinces }}§! "
    "provinces (current: [Get_{{ region.region }}_TriumphProgress]) owned by you or your subjects."
    "{% endfor %}"
    "\"\n"
    )

template_loc2 = Template(
    "{% for region in regions %}"
    " to_{{ region.region }}_triumph_progress_tt:0 \"§Y[to_{{ region.region }}_provinces.GetValue]§!\"\n"
    "{% endfor %}")

f = open(output_file, "w")
f.write(template.render(regions=regions))
f.close()

f = open(output_file_loc, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
# f.write(template_loc.render(regions=regions))
# f.write("\n")
f.write(template_loc_v2.render(regions=regions, variants=variants))
f.write(template_loc_v2_all.render(regions=regions))
f.write("\n\n")
f.write(template_loc2.render(regions=regions))
f.close()
