from jinja2 import Template, Environment

output_file = "output.txt"
output_file_local = "output_localisation.txt"
output_file_governments = "output_governments.txt"

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
		republican_tradition = 1
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
		tolerance_own = 1
		stability_cost_modifier = -0.5
	}
	effect = {
	    {{ effects }}
	}
	{{ gov_effects }}
}
\n
''')

republic = '''republic = yes
	has_term_election = no'''

republic_parliament = '''republic = yes
    has_term_election = no
    conditional = {
        allow = {
            has_dlc = "Common Sense"
        }
        has_parliament = yes
    }'''

monarchy = '''monarchy = yes
	heir = yes
	queen = yes
	republican_name = no'''

theocracy = '''has_devotion = yes
	different_religion_acceptance = -20
	different_religion_group_acceptance = -50'''

trigger_monarchy = '''
        has_reform = to_native_reform_stratified
        has_reform = to_grand_chiefdom_reform
'''

trigger_republic = '''
        OR = {
            AND = {
                NOT = { has_reform = to_native_reform_theocracy }
                has_reform = to_council_of_cities_reform
            }
            AND = {
                has_reform = to_native_reform_egalitarian
                has_reform = to_grand_chiefdom_reform
            }
        }
'''

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

general_effects = '''custom_tooltip = to_remove_excess_gov_reforms_points_tt
        custom_tooltip = to_remove_native_modifiers_tt
        hidden_effect = {
            change_government_reform_progress = -10000
            save_native_gov_reforms = yes
            change_government = native_reformed
            load_native_gov_reforms = yes
        }'''

trigger_none = '''
        OR = {
            has_reform = to_native_kingdom_reform
            AND = {
                NOT = { has_reform = to_council_of_cities_reform }
                NOT = { has_reform = to_native_parliament_reform }
                NOT = { has_reform = to_grand_chiefdom_reform }
            }
        } 
'''

variations = [("republic", republic, trigger_republic),
              ("republic_parliament", republic_parliament, trigger_republic_parliament),
              ("monarchy", monarchy, trigger_monarchy),
              ("theocracy", theocracy, trigger_theocracy),
              ("none", "", trigger_none)]

f = open(output_file, "w")
f_local = open(output_file_local, "w")
f_governments = open(output_file_governments, "w")
for variation in variations:
    f.write(codified_power.render(type=variation[0], trigger=variation[2], gov_effects=variation[1], effects=general_effects))
    name = "to_native_reform_codified_power_" + variation[0]
    f_governments.write(name + "\n")
    f_local.write(" " + name + ":0 \"Codified Power\"\n")
    f.write(government_power.render(type=variation[0], trigger=variation[2], gov_effects=variation[1], effects=general_effects))
    name = "to_native_reform_government_power_" + variation[0]
    f_governments.write(name + "\n")
    f_local.write(" " + name + ":0 \"Government Decree\"\n")
    f.write(higher_powers.render(type=variation[0], trigger=variation[2], gov_effects=variation[1], effects=general_effects))
    name = "to_native_reform_higher_powers_" + variation[0]
    f_governments.write(name + "\n")
    f_local.write(" " + name + ":0 \"Divine Mandate\"\n")
f.close()
f_local.close()
f_governments.close()
