from jinja2 import Template, Environment

output_file = "customizable_loc.txt"
output_file_loc = "loc.txt"

class Region:
    def __init__(self, region, provinces, name, province, region_format="Region"):
        self.region = region
        self.provinces = provinces
        self.name = name
        self.province = province
        self.region_format = region_format
        
regions = [
    Region("anatolia_region", 25, "Anatolia", 316),
    Region("mashriq_region", 15, "Syria", 379),
    Region("egypt_region", 15, "Aigyptos", 358),
    Region("maghreb_region", 30, "Afrika", 343),
    Region("iberia_region", 30, "Spania", 217),
    Region("italy_region", 30, "Italia", 118),
    Region("france_region", 30, "Frankia", 183),
    Region("south_german_region", 30, "Ano Germania", 134, "Reg."),
    Region("carpathia_region", 15, "Pannonia", 153),
    Region("low_countries_region", 15, "Kato Germania", 92, "Reg."),
    Region("british_isles_region", 25, "Anglia", 236)
]

template = Template('''{%- for region in regions %}
defined_text = {
	name = Get_{{ region.region }}_TriumphStatus
	random = no
	text = {
		localisation_key = to_nat_y_icon_tt
		trigger = {
			to_has_completed_triumph = { REGION = {{ region.region }} }
		}
	}

	text = {
		localisation_key = to_nat_x_icon_tt
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

template_loc = Template('''{%- for region in regions %}
 to_{{ region.region }}_triumph_check_tt:0 "[Get_{{ region.region }}_TriumphStatus][{{ region.province }}.GetRegionName] {{ region.region_format }} (§YTriumph for {{ region.name }}§!):\\n§Y{{ region.provinces }}§! provinces (current: [Get_{{ region.region }}_TriumphProgress]) owned by you or your subjects."
{%- endfor %}
''')

template_loc2 = Template('''{%- for region in regions %}
 to_{{ region.region }}_triumph_progress_tt:0 "§Y[to_{{ region.region }}_provinces.GetValue]§!" 
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render(regions=regions))
f.close()

f = open(output_file_loc, "w")
f.write(template_loc.render(regions=regions))
f.write("\n")
f.write(template_loc2.render(regions=regions))
f.close()
