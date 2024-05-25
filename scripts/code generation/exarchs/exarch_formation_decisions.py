import os
import string

from jinja2 import Template
from exarchs import exarchs

output = "o_exarch_formation_decisions.txt"
output_loc = "o_exarch_formation_localisation.txt"
output_cl = "o_exarch_formation_cl.txt"

exarchs_filtered = []

for exarch in exarchs:
    if 'special' in exarch:
        continue
    if "loc" not in exarch:
        exarch["loc"] = exarch['name'].replace("_", " ")
        exarch["loc"] = string.capwords(exarch["loc"])
    exarchs_filtered.append(exarch)

decisions_template = Template('''{% for exarch in exarchs %}
    # {{ exarch['loc'] }}
    to_form_exarch_{{ exarch['name'] }} = {
		potential = {
			nhs_check_all_elysian_tags = { CONDITION = tag }
			NOT = { exists = {{ exarch['tag'] }} }
			any_owned_province = {
				nhs_{{ exarch['tag'] }}_province = yes
				NOT = { has_province_flag = nhs_exarch_province_exemption }
			}
		}
		
		provinces_to_highlight = {
		    nhs_{{ exarch['tag'] }}_province = yes
		    OR = {
		        NOT = { owned_by = ROOT }
		        AND = {
		        	NOT = { is_state_core = ROOT }
                    NOT = { has_construction = core }
                    is_owned_by_trade_company = no
                    {%- if 'check_supply_lines' in exarch %}
                    NOT = { has_province_modifier = nhs2_supply_lines_tm }
                    {%- endif %}    
		        }
		    }
		}

		allow = {
		    if = {
		        limit = {
		            has_country_flag = to_annexed_exarch{{ exarch['tag'] }}
		        }
		        custom_trigger_tooltip = {
                    tooltip = to_has_not_annexed_exarch_in_5_years_{{ exarch['tag'] }}_tt
                    had_country_flag = {
                        flag = to_annexed_exarch{{ exarch['tag'] }}
                        days = 1825
                    }
                }
		    }
		    {%- if 'gibraltar_check' in exarch %}
            if = {
				limit = {
					226 = {
						has_province_flag = nhs_exarch_province_exemption
					}
				}
				any_owned_province = {
					nhs_{{ exarch['tag'] }}_province = yes
					NOT = { is_state_core = ROOT }
					NOT = { has_construction = core }
					is_owned_by_trade_company = no
					NOT = { province_id = 226 }
					{%- if 'check_supply_lines' in exarch %}
				    NOT = { has_province_modifier = nhs2_supply_lines_tm }
				    {%- endif %}
				}
			}
			else = {
				any_owned_province = {
					nhs_{{ exarch['tag'] }}_province = yes
					custom_trigger_tooltip = {
					    tooltip = to_is_not_state_core_of_ROOT_tt
					    NOT = { is_state_core = ROOT }
					}
					NOT = { has_construction = core }
					is_owned_by_trade_company = no
					{%- if 'check_supply_lines' in exarch %}
				    NOT = { has_province_modifier = nhs2_supply_lines_tm }
				    {%- endif %}
				}
			}
			{%- elif 'varangians_check' in exarch %}
            if = {
				limit = {
					126 = {
					    owned_by = ROOT
						has_province_modifier = to_varangian_headquarters
					}
				}
				any_owned_province = {
					nhs_{{ exarch['tag'] }}_province = yes
					NOT = { is_state_core = ROOT }
					NOT = { has_construction = core }
					is_owned_by_trade_company = no
					NOT = { has_province_modifier = to_varangian_headquarters }
					{%- if 'check_supply_lines' in exarch %}
				    NOT = { has_province_modifier = nhs2_supply_lines_tm }
				    {%- endif %}
				}
			}
			else = {
				any_owned_province = {
					nhs_{{ exarch['tag'] }}_province = yes
					NOT = { is_state_core = ROOT }
					NOT = { has_construction = core }
					is_owned_by_trade_company = no
					{%- if 'check_supply_lines' in exarch %}
				    NOT = { has_province_modifier = nhs2_supply_lines_tm }
				    {%- endif %}
				}
			}
            {%- else %}
			any_owned_province = {
				nhs_{{ exarch['tag'] }}_province = yes
				NOT = { is_state_core = ROOT }
				NOT = { has_construction = core }
				is_owned_by_trade_company = no
				{%- if 'check_supply_lines' in exarch %}
				NOT = { has_province_modifier = nhs2_supply_lines_tm }
				{%- endif %}
			}
			{%- endif %}
		}

		effect = {
		    custom_tooltip = to_exarch_starting_land_{{ exarch['tag'] }}_tt
			custom_tooltip = to_exarchate_starting_exclusions_tt
			custom_tooltip = nhs_new_line_tt
			
			custom_tooltip = nhs_exarchate_setting_desc_tt
			custom_tooltip = nhs_new_line_tt
						
			to_initialize_exarch = { EXARCH_TAG = {{ exarch['tag'] }} }
			{%- if 'additional_effects' in exarch %}
			{{ exarch["additional_effects"]}}
			{%- endif %}
			custom_tooltip = nhs_new_line_tt
			{{ exarch['tag'] }} = {
				custom_tooltip = to_set_exarch_reform_republic_tt
			}
			custom_tooltip = to_reform_effects_for_overlord_tt
			if = {
			    limit = {
			        mission_completed = to_the_eagle_rises_mission
			    }
			    custom_tooltip = to_reduce_overlord_govcap_exarch_reduced_tt
			    custom_tooltip = to_reduce_overlord_forcelimit_exarch_reduced_tt
			}
			else = {
			    custom_tooltip = to_reduce_overlord_govcap_exarch_tt
			    custom_tooltip = to_reduce_overlord_forcelimit_exarch_tt
			}
			{%- if 'merchant_tooltip_overwrite' in exarch %}
			{{ exarch["merchant_tooltip_overwrite"]}}
			{%- else %}
			custom_tooltip = to_exarch_bonus_merchant_tt
			{%- endif %}
			custom_tooltip = nhs_new_line_tt
			
			custom_tooltip = to_reform_effects_tt
			custom_tooltip = to_automatically_accepts_culture_tt
			custom_tooltip = to_min_autonomy_exarch_modifier_tt
			custom_tooltip = nhs_new_line_tt

			custom_tooltip = to_reform_modifiers_tt
			custom_tooltip = to_exarch_reform_modifiers_tt
			custom_tooltip = nhs_new_line_tt

			custom_tooltip = to_reform_government_attributes_tt
			custom_tooltip = to_exarch_reform_government_attributes_tt
		}
		ai_will_do = {
            factor = 1
        }
	}
{% endfor %}
''')

template_loc = Template("{% for exarch in exarchs %}"
                        " to_form_exarch_{{ exarch['name'] }}_title:0 \"£icon_text_elysian_subject£ "
                        "Establish the Exarchate of {{ exarch['loc'] }}"
                        "\"\n"
                        " to_form_exarch_{{ exarch['name'] }}_desc:0 \""
                        "{{ exarch['desc'] }}"
                        "\"\n"
                        " to_has_not_annexed_exarch_in_5_years_{{ exarch['tag'] }}_tt:0 \""
                        "Has NOT annexed the Exarch of §Y[{{ exarch['tag'] }}.GetName]§! in last §Y5§! years"
                        "\"\n"
                        "{% endfor %}"
                        )

# f = open(output, "w", encoding="utf-8")
# f.write(f"    # Code generated by {os.path.basename(__file__)}")
# f.write(decisions_template.render(exarchs=exarchs_filtered))
# f.close()

TEXT_COLOR = ""
TEXT_COLOR_STOP = ""
HIGHLIGHT = "§Y"
HIGHLIGHT_STOP = "§!"
ANTI_HIGHLIGHT = "§g"
ANTI_HIGHLIGHT_STOP = "§!"

# STARTING_LAND_LOC = f"{TEXT_COLOR}The Exarch receives {HIGHLIGHT}all non-core{HIGHLIGHT_STOP} provinces in"
STARTING_LAND_LOC = f"{TEXT_COLOR}The Exarch can receive any province in"

f = open(output_loc, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write(template_loc.render(exarchs=exarchs_filtered))
for exarch in exarchs_filtered:
    land_string = (exarch['land'].replace("[H]", HIGHLIGHT).replace("[!H]", HIGHLIGHT_STOP)
                   .replace("[A]", ANTI_HIGHLIGHT).replace("[!A]", ANTI_HIGHLIGHT_STOP))
    f.write(f" to_exarch_starting_land_{exarch['tag']}_tt:0 \"{STARTING_LAND_LOC} {land_string}.{TEXT_COLOR_STOP}\"\n")
    f.write(f" to_exarch_land_{exarch['tag']}_tt:0 \"{land_string}\"\n")
    if 'merchant_land' in exarch:
        merchant_land = (exarch['merchant_land'].replace("[H]", HIGHLIGHT).replace("[!H]", HIGHLIGHT_STOP)
                         .replace("[A]", ANTI_HIGHLIGHT).replace("[!A]", ANTI_HIGHLIGHT_STOP))
        f.write(f" to_exarch_merchant_land_{exarch['tag']}_tt:0 \"{merchant_land}\"\n")
    else:
        f.write(f" to_exarch_merchant_land_{exarch['tag']}_tt:0 \"{land_string}\"\n")
f.close()

f = open(output_cl, "w", encoding="utf-8")
f.write("defined_text = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write("	name = GetExarchLand\n"
        "	random = no\n\n")
for exarch in exarchs_filtered:
    f.write(f"	text = {{\n"
            f"		localisation_key = to_exarch_land_{exarch['tag']}_tt\n"
            f"		trigger = {{ tag = {exarch['tag']} }}\n"
            f"	}}\n")
f.write("}\n\n")

f.write("defined_text = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write("	name = GetExarchLandFrom\n"
        "	random = no\n\n")

for exarch in exarchs_filtered:
    f.write(f"	text = {{\n"
            f"		localisation_key = to_exarch_land_{exarch['tag']}_tt\n"
            f"		trigger = {{ FROM = {{ tag = {exarch['tag']} }} }}\n"
            f"	}}\n")
f.write("}\n\n")
f.write("defined_text = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write("	name = GetExarchMerchantLandFromProvince\n"
        "	random = no\n\n")
for exarch in exarchs_filtered:
    f.write(f"	text = {{\n"
            f"		localisation_key = to_exarch_merchant_land_{exarch['tag']}_tt\n"
            f"		trigger = {{ nhs_{exarch['tag']}_province = yes }}\n"
            f"	}}\n")
f.write("}\n\n")

f.close()
