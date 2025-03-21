import os
from jinja2 import Template

output_cl = "o_trade_node_control_cl.txt"
output_loc = "o_trade_node_control_loc.txt"

trade_nodes = [
    {
        "name": "ivory_coast",
        "loc": "Ivory Coast",
        "province": 1466,
        "cot_region": "trade_company_region = trade_company_west_africa",
        "share": 66,
        "n_cot": 5
    },
    {
        "name": "cape_of_good_hope",
        "loc": "Cape of Good Hope",
        "province": 1460,
        "cot_region": "trade_company_region = trade_company_south_africa",
        "share": 66,
        "n_cot": 1
    },
    {
        "name": "zanzibar",
        "loc": "Zanzibar",
        "province": 1448,
        "cot_region": "trade_company_region = trade_company_east_africa",
        "share": 66,
        "n_cot": 5
    },
    {
        "name": "gulf_of_aden",
        "loc": "Gulf of Aden",
        "province": 4346,
        "cot_region": "trade_company_region = trade_company_gulf_of_aden",
        "share": 66,
        "n_cot": 2
    },
    {
        "name": "alexandria",
        "loc": "Alexandria",
        "province": 358,
        "cot_region": "trade_company_region = trade_company_alexandria",
        "share": 66,
        "n_cot": 2
    },
    {
        "name": "tunis",
        "loc": "Tunis",
        "province": 341,
        "cot_region": "trade_company_region = trade_company_tunis",
        "share": 66,
        "n_cot": 1
    },
    {
        "name": "sevilla",
        "loc": "Sevilla",
        "province": 1293,
        "cot_region": "trade_company_region = trade_company_sevilla",
        "share": 66,
        "n_cot": 2
    }
    , {
        "name": "polynesia_node",
        "loc": "Polynesian Triangle",
        "province": 1997,
        "cot_region": "region = oceanea_region",
        "share": 80,
        "n_cot": 2
    },
    {
        "name": "philippines",
        "loc": "Philippines",
        "province": 1397,
        "cot_region": "trade_company_region = trade_company_philippines",
        "share": 80,
        "n_cot": 5
    }
]

template_cl = Template('''{%- for trade_node in trade_nodes %}
defined_text = {
	name = Has_{{ trade_node['share'] }}_in_{{ trade_node['name'] }}
	random = no
	text = {
		localisation_key = to_y_icon_tt
		trigger = {
			{{ trade_node['province'] }} = {
                trade_share = {
                    country = ROOT
                    share = {{ trade_node['share'] }}
                }
            }
		}
	}
	text = {
		localisation_key = to_x_icon_tt
	}
}
defined_text = {
	name = Has_{{ trade_node['n_cot'] }}_cot_in_{{ trade_node['name'] }}
	random = no
	text = {
		localisation_key = to_y_icon_tt
		trigger = {
		    calc_true_if = {
                amount = {{ trade_node['n_cot'] }}
                all_province = {
                    {{ trade_node['cot_region'] }}
                    province_has_center_of_trade_of_level = 1
                    country_or_subject_or_ally_or_ally_subject_holds = { TAG = ROOT }
                }
			}
		}
	}
	text = {
		localisation_key = to_x_icon_tt
	}
}
{%- endfor %}''')

template_loc = Template("{%- for trade_node in trade_nodes %}"
                        " to_controls_{{ trade_node['name'] }}_tt:0 \""
                        "§Y{{ trade_node['loc'] }}§! Trade Node:\\n"
                        "       [Root.Has_{{ trade_node['share'] }}_in_{{ trade_node['name'] }}]"
                        "Has at least §Y{{ trade_node['share'] }}%§! Trade Share.\\n"
                        "       [Root.Has_{{ trade_node['n_cot'] }}_cot_in_{{ trade_node['name'] }}]"
                        "At least §Y{{ trade_node['n_cot'] }}§! "
                        "Center(s) of Trade fully owned by us,\\n            our Subject or Allies."
                        "\"\n"
                        "{% endfor %}"
                        )

f = open(output_cl, "w")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}")
f.write(template_cl.render(trade_nodes=trade_nodes))
f.close()

f = open(output_loc, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write(template_loc.render(trade_nodes=trade_nodes))
f.close()