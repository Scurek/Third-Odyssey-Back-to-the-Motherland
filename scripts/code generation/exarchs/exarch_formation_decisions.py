import os
import string

from jinja2 import Template
from exarchs import exarchs

output = "o_exarch_formation_decisions.txt"
output_loc = "o_exarch_formation_localisation.txt"

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
					NOT = { is_state_core = ROOT }
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
			custom_tooltip = nhs_exarchate_starting_tt
			custom_tooltip = nhs_exarchate_setting_desc_tt
			custom_tooltip = to_exarchate_modifiers_tt
			{%- if 'merchant_tooltip_overwrite' in exarch %}
			{{ exarch["merchant_tooltip_overwrite"]}}
			{%- else %}
			custom_tooltip = nhs_exarch_bonus_merchant_tt
			{%- endif %}
			custom_tooltip = nhs_new_line_tt
			
			to_initialize_exarch = {
                EXARCH_TAG = {{ exarch['tag'] }}
                CULTURE_GROUP = {{ exarch['culture_group'] }}
                PRIMARY_CULTURE = {{ exarch['primary_culture'] }}
            }
            {%- if 'additional_effects' in exarch %}
			{{ exarch["additional_effects"]}}
			{%- endif %}
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

f = open(output, "w", encoding="utf-8")
f.write(f"    # Code generated by {os.path.basename(__file__)}")
f.write(decisions_template.render(exarchs=exarchs_filtered))
f.close()

f = open(output_loc, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write(template_loc.render(exarchs=exarchs_filtered))
f.close()