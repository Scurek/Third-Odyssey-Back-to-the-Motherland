import os

from jinja2 import Template, Environment
output_file = "o_customizable_loc.txt"
output_file_loc = "o_loc.txt"
output_file_events = "o_events.txt"

jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])
file_path = f"{os.path.basename(os.getcwd())}/{os.path.basename(__file__)}"

class Region:
    def __init__(self, region, provinces, name, province, cities=None, region_format="Region", order=0,
                 event_picture="BYZANTINE_EAGLE_eventPicture"):
        self.region = region
        self.provinces = provinces
        self.name = name
        self.province = province
        self.region_format = region_format
        self.cities = cities
        self.order = order
        self.event_picture = event_picture


regions = [
    Region("anatolia_region", 30, "Anatolia", 316, [318, 317]),  # Total 48
    Region("mashriq_region", 20, "Syria", 379, [2313]),  # Total 30
    Region("egypt_region", 20, "Aigyptos", 358, [358]),  # Total 29
    Region("maghreb_region", 30, "Afrika", 343, [341]),  # Total 63
    Region("iberia_region", 40, "Spania", 217, [225, 213]),  # Total 62 | 218, 220
    Region("italy_region", 40, "Italia", 118, [118, 104, 114],
           event_picture="TO_TRIUMPH_IN_MILAN_eventPicture"), # Total 57
    Region("france_region", 40, "Frankia", 183, [183, 203],
           event_picture="TO_TRIUMPH_IN_PARIS_eventPicture"),  # Total 66
    Region("south_german_region", 40, "Ano Germania", 134, [134, 1868], region_format="Reg."),  # Total 64
    Region("british_isles_region", 30, "Anglia", 236, [236],
           event_picture="TO_TRIUMPH_IN_LONDON_eventPicture"),  # Total 56
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
			{%- if region.cities is not none %}
			{%- for city in region.cities %}
			owns_or_subject_of = {{ city }}
			{%- endfor %}
			{%- endif %}
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

defined_text = {
	name = Get_{{ region.region }}_TooltipColor
	random = no
	text = {
		localisation_key = to_green_tt
		trigger = {
            check_variable = {
                which = to_{{ region.region }}_provinces
                value = {{ region.provinces }}
            }
		}
	}

	text = {
		localisation_key = to_yellow_tt
	}
}

{%- if region.cities is not none %}
{% for city in region.cities %}
defined_text = {
	name = Get_{{ city }}_TooltipColor
	random = no
	text = {
		localisation_key = to_green_tt
		trigger = {
            owns_or_subject_of = {{ city }}
		}
	}

	text = {
		localisation_key = to_yellow_tt
	}
}
{% endfor %}
{%- endif %}

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

template_loc_v3 = jinja_env.from_string(
    "{% for i in range(variants) %}"
    "to_triumphs_completed_count_var_{{ i }}_tt:0 \""
    " Triumphs Completed:\\n§gEach Triumph requires direct or subject ownership of one or more specific "
    "cities and certain number of provinces within a region.§!"
    "{% for region in regions %}"
    "{% if i < region.order %}{% continue %}{% endif %}"
    "\\n"
    "  [Get_{{ region.region }}_TriumphStatus][{{ region.province }}.GetRegionName]: "
    "[Get_{{ region.region }}_TriumphProgress]/§Y{{ region.provinces }}§! provinces reconquered,"
    "{% if region.cities is not none %}"
    "\\nKey Cities: "
    "{% for city in region.cities %}"
    "{% if loop.last and not loop.first %}"
    " and "
    "{% elif not loop.first %}"
    ", "
    "{% endif %}"
    "§Y[{{ city }}.GetName]§!"
    "{% endfor %}"
    "{% endif %}"
    "{% endfor %}"
    "\"\n\n"
    "{% endfor %}"
    )

template_loc_v4 = jinja_env.from_string(
    "{% for i in range(variants) %}"
    " to_triumphs_completed_count_var_{{ i }}_tt:0 \" "
    "Triumphs Completed:\\n§gEach Triumph requires direct or subject ownership of one or more specific "
    "cities and certain number of provinces within a region.§!"
    "{% for region in regions %}"
    "{% if i < region.order %}{% continue %}{% endif %}"
    "\\n"
    " [Get_{{ region.region }}_TriumphStatus]§Y[{{ region.province }}.GetRegionName]§!, "
    "{% if region.cities is not none %}"
    "key cities: "
    "{% for city in region.cities %}"
    "{% if loop.last and not loop.first %}"
    " and "
    "{% elif not loop.first %}"
    ", "
    "{% endif %}"
    "[Get_{{ city }}_TooltipColor][{{ city }}.GetName]§!"
    "{% endfor %}"
    "{% endif %}"
    ",\\n      "
    "§Y{{ region.provinces }}§! "
    "provinces (currently: [Get_{{ region.region }}_TriumphProgress]) reconquered."
    "{% endfor %}"
    "\"\n\n"
    "{% endfor %}"
    )

template_loc_v4_all = jinja_env.from_string(
    " to_triumphs_completed_all_tt:0 \""
    "All Triumphs have been completed:\\n§gEach Triumph requires direct or subject ownership of one or more specific "
    "cities and certain number of provinces within a region.§!"
    "{% for region in regions %}"
    "\\n"
    " [Get_{{ region.region }}_TriumphStatus]§Y[{{ region.province }}.GetRegionName]§!, "
    "{% if region.cities is not none %}"
    "key cities: "
    "{% for city in region.cities %}"
    "{% if loop.last and not loop.first %}"
    " and "
    "{% elif not loop.first %}"
    ", "
    "{% endif %}"
    "[Get_{{ city }}_TooltipColor][{{ city }}.GetName]§!"
    "{% endfor %}"
    "{% endif %}"
    ",\\n      "
    "§Y{{ region.provinces }}§! "
    "provinces (currently: [Get_{{ region.region }}_TriumphProgress]) reconquered."
    "{% endfor %}"
    "\"\n\n"
    )

template_loc2 = Template(
    "{% for region in regions %}"
    " to_{{ region.region }}_triumph_progress_tt:0 \""
    "[Get_{{ region.region }}_TooltipColor][to_{{ region.region }}_provinces.GetValue]§!\"\n"
    "{% endfor %}")

template_loc_triumph_modifiers = Template(
    "{% for region in regions %}"
    " to_increase_culture_integration_{{ region.region }}_tt:0 \""
    " Increases the monthly progress of culture integration in §Y[{{ region.province }}.GetRegionName]§! by §G50.0%§!."
    "\"\n"
    " to_{{ region.region }}_warscore_cost_red_tt:0 \""
    "Every province in §Y[{{ region.province }}.GetRegionName]§! gains '§YTriumph Declared§!' modifier, "
    "giving the following effect:\\n"
    " War Score Cost: §G-20.0%§!\"\n"
    "{% endfor %}")

f = open(output_file, "w")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}")
f.write(template.render(regions=regions))
f.close()

f = open(output_file_loc, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
# f.write(template_loc.render(regions=regions))
# f.write("\n")
f.write(template_loc_v4.render(regions=regions, variants=variants))
f.write(template_loc_v4_all.render(regions=regions))
f.write("\n\n")
f.write(template_loc2.render(regions=regions))
f.write("\n\n")
f.write(template_loc_triumph_modifiers.render(regions=regions))
f.close()


## EVENTS
start_id = 27
namespace = "nhs_mission_events"


template_events = Template('''{%- for region in regions %}
# Triumph for {{ region.name }}
# Code generated by {{ file_path }}
country_event = {
	id = {{ namespace }}.{{ start_id + loop.index0 }}
	title = {{ namespace }}.{{ start_id + loop.index0 }}.t
	desc = {{ namespace }}.{{ start_id + loop.index0 }}.d
	picture = {{ region.event_picture }}
	
	trigger = {
	    nhs_check_all_elysian_tags = { CONDITION = tag }
        mission_completed = to_heir_of_justinian_mission
		to_has_completed_triumph = { REGION = {{ region.region }} }
        {%- if region.cities is not none %}
        {%- for city in region.cities %}
        owns_or_subject_of = {{ city }}
        {%- endfor %}
        {%- endif %}
        NOT = { has_country_flag = to_triumph_for_{{ region.region }} }
        OR = {
			NOT = { has_country_flag = to_recent_triumph }
			had_country_flag = { flag = to_recent_triumph days = 10 }
		}
	}
	
	immediate = {
		hidden_effect = {
		    set_country_flag = to_triumph_for_{{ region.region }}
		    clr_country_flag = to_recent_triumph
			set_country_flag = to_recent_triumph
		}
	}

	option = {
		name = to_triumph_event.a
		if = {
		    limit = {
		        has_regency = yes    
		    }
		    custom_tooltip = to_only_option_due_to_regency_tt
		    custom_tooltip = nhs_new_line_tt
		}
		add_prestige = 10
		add_army_tradition = 10
		custom_tooltip = nhs_dotted_line_tt
		if = {
		    limit = { to_enabled_european_culture_integration = yes }
		    custom_tooltip = to_increase_culture_integration_{{ region.region }}_tt
		}
		custom_tooltip = to_{{ region.region }}_warscore_cost_red_tt
		hidden_effect = {
			every_province = {
				limit = {
					region = {{ region.region }}
				}
				add_permanent_province_modifier = {
					name = to_triumph_warscore_cost_red
					duration = -1
				}
			}
		}
	}

	option = {
		name = to_triumph_event.b
		trigger = {
		    has_regency = no
		}
		add_prestige = 15
		add_legitimacy = 15
		add_heir_claim = 10
		add_splendor = 25
		custom_tooltip = nhs_dotted_line_tt
		if = {
		    limit = { to_enabled_european_culture_integration = yes }
		    custom_tooltip = to_increase_culture_integration_{{ region.region }}_tt
		}
		custom_tooltip = to_{{ region.region }}_warscore_cost_red_tt
		hidden_effect = {
			every_province = {
				limit = {
					region = {{ region.region }}
				}
				add_permanent_province_modifier = {
					name = to_triumph_warscore_cost_red
					duration = -1
				}
			}
		}
	}
}
{% endfor %}
''')

f = open(output_file_events, "w")
f.write(template_events.render(regions=regions, file_path=file_path, start_id=start_id, namespace=namespace))
f.close()