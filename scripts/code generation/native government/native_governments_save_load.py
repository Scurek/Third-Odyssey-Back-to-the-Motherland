from jinja2 import Template, Environment

output_file_save = "output_save.txt"
output_file_load = "output_load.txt"

reforms = [
    "to_native_reform_egalitarian",
    "to_native_reform_stratified",
    # "to_native_reform_theocracy",
    "native_martial_tradition_reform",
    "native_oral_tradition_reform",
    "native_land_tradition_reform",
    "native_seasonal_travel_reform",
    "native_settle_down_reform",
    "native_war_band_reform",
    "to_native_reform_nomadic_raiders",
    "to_native_reform_consensus_government",
    "to_native_reform_law_of_peace",
    "to_native_reform_grand_chiefdom",
    "to_native_reform_kingdom",
    "to_native_reform_codified_power",
    "to_native_reform_government_power",
    "to_native_reform_higher_powers",
]

save = Template('''{% for reform in reforms %}
    if = { limit = { has_reform = {{ reform }} } 
        set_country_flag = to_had_native_reform_{{ reform }} }
{%- endfor %}
''')

load = Template('''{% for reform in reforms %}
    if = { limit = { has_country_flag = to_had_native_reform_{{ reform }} } 
        add_government_reform = {{ reform }}
        clr_country_flag = to_had_native_reform_{{ reform }}
    }
{%- endfor %}
''')

f = open(output_file_save, "w")
f.write(save.render(reforms=reforms))
f.close()

f = open(output_file_load, "w")
f.write(load.render(reforms=reforms))
f.close()
