from jinja2 import Template, Environment

output_file = "output.txt"
output_file_local = "output_localisation.txt"
output_file_governments = "output_governments.txt"
output_file_array = "output_array.txt"

# sequence = range(5000, 0, -STEP)

codified_power = Template('''to_native_reform_codified_power_{{ type }} = {
	icon = "federal_constitution"
	allow_normal_conversion = yes
	valid_for_nation_designer = yes
	nation_designer_cost = 20
	potential = { {{ trigger }} \t}
	modifiers = {
		legitimacy = 1
		monthly_heir_claim_increase = 0.5
		republican_tradition = 0.5
		horde_unity = 2
	}
	effect = {
	    {{ effects }}
	}
	{{ gov_effects }}
}
\n
''')

government_power = Template('''to_native_reform_government_power_{{ type }} = {
	icon = "organising_our_religion_reform"
	allow_normal_conversion = yes
	valid_for_nation_designer = yes
	nation_designer_cost = 20
	potential = { {{ trigger }} \t}
	modifiers = {
		all_power_cost = -0.05
		monthly_reform_progress_modifier = -0.2
	}
	effect = {
	    {{ effects }}
	}
	{{ gov_effects }}
}
\n
''')

higher_powers = Template('''to_native_reform_higher_powers_{{ type }} = {
	icon = "native_codified_power_reform"
	allow_normal_conversion = yes
	valid_for_nation_designer = yes
	nation_designer_cost = 20
	potential = { {{ trigger }} \t}
	modifiers = {
		tolerance_own = 2
		stability_cost_modifier = -0.33
	}
	effect = {
	    {{ effects }}
	}
	{{ gov_effects }}
}
\n
''')

republic = '''republic = yes
	has_term_election = no
	custom_attributes = {
		election_on_death = yes
	}'''

republic_parliament = '''republic = yes
    has_term_election = no
    conditional = {
        allow = {
            has_dlc = "Common Sense"
        }
        has_parliament = yes
    }'''

monarchy = '''monarchy = yes
    # heir = no
	republican_name = no'''

theocracy = '''has_devotion = yes
	different_religion_acceptance = -20
	different_religion_group_acceptance = -50'''

effect_republic = '''
        hidden_effect = {
            add_republican_tradition = 80
        }
'''

effect_theocracy = '''
        add_devotion = 80
'''

effect_monarchy = '''
        if = {
            limit = {
                has_ruler_flag = to_nat_has_native_council
            }
            define_ruler = {
                claim = 80
                min_age = 30
                max_age = 60
            }
        }
        else = {
            hidden_effect = {
                add_legitimacy = -100
                add_legitimacy = 80
            }
        }
'''

trigger_monarchy = '''
        has_reform = to_native_kingdom_reform
'''

# trigger_monarchy = '''
#         has_reform = to_native_reform_stratified
#         has_reform = to_grand_chiefdom_reform
# '''

trigger_republic = '''
        OR = {
            has_reform = to_native_parliament_reform
            has_reform = to_council_of_cities_reform
            has_reform = to_grand_chiefdom_reform
        }
'''

# trigger_republic = '''
#         OR = {
#             has_reform = to_native_parliament_reform
#             AND = {
#                 NOT = { has_reform = to_native_reform_theocracy }
#                 has_reform = to_council_of_cities_reform
#             }
#             AND = {
#                 has_reform = to_native_reform_egalitarian
#                 has_reform = to_grand_chiefdom_reform
#             }
#         }
# '''

trigger_republic_parliament = '''
        has_reform = to_native_parliament_reform
'''

trigger_theocracy = '''
        has_reform = to_native_reform_theocracy
        OR = {
            has_reform = to_grand_chiefdom_reform
            has_reform = to_council_of_cities_reform
        }
'''

general_effects = '''if = {
            limit = {
                has_reform = native_basic_reform
            }
            custom_tooltip = to_remove_excess_gov_reforms_points_tt
            custom_tooltip = to_remove_native_modifiers_tt
            hidden_effect = {
                to_save_native_reforms = yes
                change_government = native_reformed
                to_load_native_reforms = yes
                change_government_reform_progress = -10000
            }
        }'''

trigger_none = '''
        NOT = { has_reform = to_native_kingdom_reform }
        NOT = { has_reform = to_council_of_cities_reform }
        NOT = { has_reform = to_native_parliament_reform }
        NOT = { has_reform = to_grand_chiefdom_reform }
'''
# trigger_none = '''
#         OR = {
#             has_reform = to_native_kingdom_reform
#             AND = {
#                 NOT = { has_reform = to_council_of_cities_reform }
#                 NOT = { has_reform = to_native_parliament_reform }
#                 NOT = { has_reform = to_grand_chiefdom_reform }
#             }
#         }
# '''
governments = [(codified_power, "to_native_reform_codified_power_", "Codified Power"),
               (government_power, "to_native_reform_government_power_", "Government Decree"),
               (higher_powers, "to_native_reform_higher_powers_", "Divine Mandate")]

variations = [("republic", republic, trigger_republic, effect_republic),
              # ("republic_parliament", republic_parliament, trigger_republic_parliament, effect_republic),
              ("monarchy", monarchy, trigger_monarchy, effect_monarchy),
              # ("theocracy", theocracy, trigger_theocracy, effect_theocracy),
              ("none", "", trigger_none, "")]

f = open(output_file, "w")
f_local = open(output_file_local, "w")
f_governments = open(output_file_governments, "w")
f_array = open(output_file_array, "w")
for variation in variations:
    for government in governments:
        f.write(government[0].render(type=variation[0], trigger=variation[2], gov_effects=variation[1],
                                     effects=general_effects + variation[3]))
        name = government[1] + variation[0]
        f_array.write("\"" + name + "\",\n")
        f_governments.write(name + "\n")
        f_local.write(" " + name + ":0 \"" + government[2] + "\"\n")

f.close()
f_local.close()
f_governments.close()
f_array.close()
