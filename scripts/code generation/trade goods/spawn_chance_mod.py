from trade_goods import trade_goods
from jinja2 import Template
import string
import os

localisation_output = "o_loc_trade_goods_mod.txt"
cl_output = "o_cl_trade_goods_mod.txt"
interface_output = "o_interface_trade_goods_mod.txt"
interface_tdo_output = "o_interface_tdo_trade_goods_mod.txt"
events_output = "o_events_trade_goods_mod.txt"

main_event_tag = "nhs_mission_events.3"
event_picture = "TRADE_GOODS_PLANTATION_GOODS_IN_WAREHOUSE_eventPicture"
option_tags = ["a", "b", "c", "d", "e", "f", "g"]
groups = [
    {
        "title": "Aliments",
        "name": "aliments",
        "event_id": "nhs_mission_events.4",
        "option_tag": "a",
        "pad_left": 5,
        "members": [
            "grain",
            "livestock",
            "fish",
            "wine",
            "salt"
        ]
    },
    {
        "title": "Cash Crops",
        "name": "cash_crops",
        "event_id": "nhs_mission_events.5",
        "option_tag": "b",
        "pad_left": 12,
        "members": [
            "sugar",
            "tobacco",
            "tea",
            "coffee",
            "cocoa",
        ]
    },
    {
        "title": "Natural Resources",
        "name": "natural_resources",
        "event_id": "nhs_mission_events.6",
        "option_tag": "c",
        "pad_left": 5,
        "members": [
            "iron",
            "copper",
            "gold",
            "gems",
            "naval_supplies"
        ]
    },
    {
        "title": "Luxuries",
        "name": "luxuries",
        "event_id": "nhs_mission_events.7",
        "option_tag": "e",
        "pad_left": 12,
        "members": [
            "spices",
            "chinaware",
            "incense",
            "ivory",
            "tropical_wood"
        ]
    },
    {
        "title": "Textiles",
        "name": "textiles",
        "event_id": "nhs_mission_events.8",
        "option_tag": "f",
        "pad_left": 43,
        "members": [
            "cotton",
            "wool",
            "fur",
            "dyes"
        ]
    },
]

for group in groups:
    for i, member in enumerate(group['members']):
        for trade_good in trade_goods:
            if trade_good["name"] == member:
                group['members'][i] = trade_good
                member = trade_good
                continue
        if "loc" not in member:
            member["loc"] = member["name"].replace("_", " ")
            member["loc"] = string.capwords(member["loc"])

main_event_loc = Template(" {{ main_event_tag }}.t:0 \"Trade Goods Management\""
                          "\n"
                          " {{ main_event_tag }}.d:0 \"£background_square£\\n"
                          "{%- for group in groups %}"
                          "{% if loop.index is not divisibleby 2 %}"
                          "£{{ group['name'] }}_banner£"
                          "{% if not loop.last %}"
                          "£{{ loop.nextitem['name'] }}_banner£"
                          "{% endif %}"
                          "\\n\\n"
                          "{%- for _ in range(group['pad_left']) %}"
                          " "
                          "{% endfor %}"
                          "{%- for member in group['members'] %}"
                          "[Root.Check_{{ member['name'] }}_selected]"
                          "{% endfor %}"
                          "{% if not loop.last %}"
                          "{%- for _ in range(loop.nextitem['pad_left']) %}"
                          " "
                          "{% endfor %}"
                          "{%- for member in loop.nextitem['members'] %}"
                          "[Root.Check_{{ member['name'] }}_selected]"
                          "{% endfor %}"
                          "\\n\\n\\n"
                          "{% endif %}"
                          "{% endif %}"
                          "{% endfor %}"
                          "\"\n"
                          "{% for group in groups %}"
                          " {{ main_event_tag }}.{{ group['option_tag'] }}:0 \""
                          "{{ group['title'] }} "
                          "{% for member in group['members'] %}"
                          "£icon_tg_{{ member['name'] }}£"
                          "{% endfor %}"
                          "\"\n"
                          "{% endfor %}"
                          " {{ main_event_tag }}.g:0 \"Back\"\n"
                          )

groups_events = Template("{%- for main_group in groups %}"
                         # " {{ main_group['event_id'] }}.t:0 \"Trade Goods Management\""
                         # "\n"
                         # " {{ main_group['event_id'] }}.d:0 \""
                         # "{%- for group in groups %}"
                         # "£{{ group['name'] }}_banner£\\n\\n"
                         # "{%- for member in group['members'] %}"
                         # "[Root.Check_{{ member['name'] }}_selected]"
                         # "{% endfor %}"
                         # "{% if loop.index is divisibleby 2 %}"
                         # "\\n\\n"
                         # "{% endif %}"
                         # "{% endfor %}"
                         # "\"\n"
                         "{% for i in range(main_group['members'] | length) %}"
                         " {{ main_group['event_id'] }}.{{ option_tags[i] }}:0 "
                         "\"{{ main_group['members'][i]['loc'] }} "
                         "£icon_tg_{{ main_group['members'][i]['name'] }}£\""
                         "\n"
                         "{% endfor %}"
                         # " {{ main_group['event_id'] }}.{{ option_tags[main_group['members'] | length] }}:0"
                         # " \"Back\"\n"
                         "{% endfor %}"
                         )

selected_loc = Template("{%- for trade_good in trade_goods %}"
                        "{% if 'no_circle_icon' is not in trade_good %}"
                        " {{ trade_good['name'] }}_circle_selected_tt:0 "
                        "\"£circle_{{ trade_good['name'] }}_selected£\""
                        "\n"
                        " {{ trade_good['name'] }}_circle_tt:0 "
                        "\"£circle_{{ trade_good['name'] }}£\""
                        "\n"
                        "{% endif %}"
                        "{% endfor %}"
                        )

tooltips_loc = Template("{%- for trade_good in trade_goods %}"
                        "{% if 'no_circle_icon' is not in trade_good %}"
                        " to_restore_spawn_chance_of_{{ trade_good['name'] }}_tt:0 \""
                        "Restores the chance of discovering §Y{{ trade_good['loc'] }}§! back to normal."
                        "\"\n"
                        " to_increase_spawn_chance_of_{{ trade_good['name'] }}_tt:0 \""
                        "§YQuadruples§! the chance of discovering §Y{{ trade_good['loc'] }}§! during colonization."
                        "\"\n"
                        "{% endif %}"
                        "{% endfor %}"
                        )

tooltips_loc_groups = Template("{%- for group in groups %}"
                               " to_switch_to_{{ group['name'] }}_view_tt:0 \""
                               "Modify the discovery chance of"
                               "{%- for member in group['members'] %}"
                               " §Y{{ member['loc'] }}§!"
                               "{% if loop.revindex == 2 %}"
                               " and"
                               "{% elif not loop.last %}"
                               ","
                               "{% endif %}"
                               "{% endfor %}"
                               ".\"\n"
                               "{% endfor %}"
                               )

templateCL = Template('''{%- for trade_good in trade_goods %}
{%- if 'no_circle_icon' is not in trade_good %}
defined_text = {
	name = Check_{{ trade_good['name'] }}_selected
	random = no
	text = {
		localisation_key = {{ trade_good['name'] }}_circle_selected_tt
		trigger = {
			has_country_flag = to_increased_spawn_chance_{{ trade_good['name'] }}
		}
	}
	text = {
		localisation_key = {{ trade_good['name'] }}_circle_tt
	}
}
{%- endif %}
{%- endfor %}
''')

###

template_events = Template('''
# Trade Good Spawn Chance Modification, Main Event
# Code generated by {{ code_file_name }}
country_event = {
	id = {{ main_event_tag }}
	title = {{ main_event_tag }}.t
	desc = {{ main_event_tag }}.d
	picture = {{ event_picture }}
	
	is_triggered_only = yes
	{% for group in groups %}
	option = {
		name = {{ main_event_tag }}.{{ group['option_tag'] }}
		custom_tooltip = to_switch_to_{{ group["name"] }}_view_tt
		hidden_effect = {
		    country_event = { id = {{ group['event_id'] }} }
		}
	}
	{%- endfor %}
	option = {
		name = {{ main_event_tag }}.g
		clr_country_flag = to_trade_good_manager_open
	}
}
{%- for group in groups %}
{% for j in range(2) %}
# Trade Good Spawn Chance Modification, {{ group['title'] }} Event 1/2
# Code generated by {{ code_file_name }}
country_event = {
    {%- if j == 0 %}
	id = {{ group['event_id'] }}
	{%- else %}
	id = {{ group['event_id'] }}01
	{%- endif %}
	title = {{ main_event_tag }}.t
	desc = {{ main_event_tag }}.d
	picture = {{ event_picture }}
	
	is_triggered_only = yes
	{% for i in range(group['members'] | length) %}
	option = {
		name = {{ group['event_id'] }}.{{ option_tags[i] }}
		if = {
		    limit = {
		        has_country_flag = to_increased_spawn_chance_{{ group['members'][i]['name'] }}
		    }
		    custom_tooltip = to_restore_spawn_chance_of_{{ group['members'][i]['name'] }}_tt
		    clr_country_flag = to_increased_spawn_chance_{{ group['members'][i]['name'] }}
		}
		else = {
		    custom_tooltip = to_increase_spawn_chance_of_{{ group['members'][i]['name'] }}_tt
		    set_country_flag = to_increased_spawn_chance_{{ group['members'][i]['name'] }}
		}
		hidden_effect = {
		    {%- if j == 0 %}
		    country_event = { id = {{ group['event_id'] }}01 }
		    {%- else %}
		    country_event = { id = {{ group['event_id'] }} }
		    {%- endif %}
		}
	}
	{%- endfor %}
	option = {
		name = {{ main_event_tag }}.g
		hidden_effect = {
		    country_event = { id = {{ main_event_tag }} }
		}
	}
}
{%- endfor %}
{%- endfor %}
''')

###

template_interface_icons = Template('''{%- for trade_good in trade_goods %}
{%- if 'no_icon' is not in trade_good %}
    spriteType = {
        name = "GFX_icon_tg_{{ trade_good["name"] }}"
        texturefile = "gfx//interface//text_icons//icon_tg_{{ trade_good["name"] }}.dds"
    }
{%- endif %}
{%- endfor %}
''')

template_interface_circles = Template('''{%- for trade_good in trade_goods %}
{%- if 'no_circle_icon' is not in trade_good %}
    spriteType = {
        name = "GFX_circle_{{ trade_good["name"] }}"
        texturefile = "gfx//interface//trade_good_spawn_chance//circle_{{ trade_good["name"] }}.dds"
    }
    spriteType = {
        name = "GFX_circle_{{ trade_good["name"] }}_selected"
        texturefile = "gfx//interface//trade_good_spawn_chance//circle_{{ trade_good["name"] }}_selected.dds"
    }
{%- endif %}
{%- endfor %}
''')

f = open(localisation_output, "w", encoding="utf-8")
f.write(main_event_loc.render(groups=groups, main_event_tag=main_event_tag))
f.write("\n\n")
f.write(groups_events.render(groups=groups, option_tags=option_tags))
f.write("\n")
f.write(tooltips_loc.render(trade_goods=trade_goods))
f.write(tooltips_loc_groups.render(groups=groups))
f.write("\n")
f.write(selected_loc.render(trade_goods=trade_goods))
f.close()

f = open(cl_output, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(__file__)}")
f.write(templateCL.render(trade_goods=trade_goods))
f.close()

f = open(events_output, "w", encoding="utf-8")
f.write(template_events.render(groups=groups, main_event_tag=main_event_tag, option_tags=option_tags,
                               event_picture=event_picture))
f.close()

f = open(interface_output, "w")
f.write(f"# Code generated by {os.path.basename(__file__)}")
f.write(template_interface_icons.render(trade_goods=trade_goods))
f.close()
f = open(interface_tdo_output, "w")
f.write(f"# Code generated by {os.path.basename(__file__)}")
f.write(template_interface_circles.render(trade_goods=trade_goods))
f.close()
