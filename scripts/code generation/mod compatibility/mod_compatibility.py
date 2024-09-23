import csv
import os
import re
from jinja2 import Template, Environment

output_file_loc = "o_localization.txt"
output_file_events = "o_events.txt"

COMPATIBILITY_COLUMN = 1
URL_COLUMN = 2

def parse_id(url):
    return re.search(r'id=(\d+)', url).group(1)


incompatible_mods = []
compatible_mods = []
with open('Compatibility - List1.tsv') as file:
    rd = csv.reader(file, delimiter="\t", quotechar='"')
    for i, row in enumerate(rd):
        if i == 0:
            continue
        if len(row) < 3 or row[COMPATIBILITY_COLUMN] not in ['yes', 'no']:
            continue
        mod_id = parse_id(row[URL_COLUMN])
        if row[COMPATIBILITY_COLUMN] == 'no':
            incompatible_mods.append({"name": row[0], "mod_id": mod_id})
        else:
            compatible_mods.append({"name": row[0], "mod_id": mod_id})

with open(output_file_loc, "w", encoding="utf-8-sig") as file_loc:
    file_loc.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for mod in incompatible_mods:
        file_loc.write(f" to_mod_{mod['mod_id']}_name_tt:0 \"§Y{mod['name'].replace("[", "|").replace("]", "|")}§!\"\n")
    for mod in compatible_mods:
        file_loc.write(f" to_mod_{mod['mod_id']}_name_tt:0 \"{mod['name'].replace("[", "|").replace("]", "|")}\"\n")

template = Template('''namespace = to_compatibility_check
    
country_event = {
    id = to_compatibility_check.1
    title = to_compatibility_check.1.t
    desc = to_compatibility_check.1.d
    picture = picture = TO_STEAM_WORKSHOP_eventPicture
    
    is_triggered_only = yes
    
    trigger = {
        ai = no
        if = {
            limit = {
                has_global_flag = to_only_show_incompatibility_on_differences
            }
            OR = {
                {%- for mod in incompatible_mods %}
                AND = {
                    is_mod_active = "{{ mod['name'] }}"
                    NOT = { has_global_flag = to_mod_{{ mod['mod_id'] }}_detected }
                }
                {%- endfor %}
            }
        }
        else = {
            OR = {
                {%- for mod in incompatible_mods %}
                is_mod_active = "{{ mod['name'] }}"
                {%- endfor %}
            }
        }
    }
    
    immediate = {
        hidden_effect = {
            set_global_flag = to_incompatible_mods_active
            {%- for mod in incompatible_mods %}
            if = {
                limit = {
                    is_mod_active = "{{ mod['name'] }}"
                }
                set_global_flag = to_mod_{{ mod['mod_id'] }}_detected
            }
            {%- endfor %}
        }
    }
    
    option = {
        name = to_compatibility_check.1.a
        custom_tooltip = to_incompatible_mods_active_tt
        {%- for mod in incompatible_mods %}
        if = {
            limit = {
                is_mod_active = "{{ mod['name'] }}"
            }
            custom_tooltip = to_mod_{{ mod['mod_id'] }}_name_tt
        }
        {%- endfor %}
        
        ##############
        
        if = {
            limit = {
                OR = {
                    {%- for mod in compatible_mods %}
                    is_mod_active = "{{ mod['name'] }}"
                    {%- endfor %}
                }
            }
            custom_tooltip = to_compatible_mods_active_tt
            {%- for mod in compatible_mods %}
            if = {
                limit = {
                    is_mod_active = "{{ mod['name'] }}"
                }
                custom_tooltip = to_mod_{{ mod['mod_id'] }}_name_tt
            }
            {%- endfor %}
        }
    }
    
    option = {
        name = to_compatibility_check.1.b
        custom_tooltip = to_only_show_incompatibility_on_differences_tt
        set_global_flag = to_only_show_incompatibility_on_differences
    }
}
''')

with open(output_file_events, "w") as file_events:
    file_events.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    file_events.write(template.render(incompatible_mods=incompatible_mods, compatible_mods=compatible_mods))