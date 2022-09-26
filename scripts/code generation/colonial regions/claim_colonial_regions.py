import os
import shutil
from jinja2 import Environment

output_peace_treaties = "peace_treaties"
if not os.path.isdir(output_peace_treaties):
    os.makedirs(output_peace_treaties)
else:
    shutil.rmtree(output_peace_treaties)
    os.makedirs(output_peace_treaties)

output_loc = "o_colonial_region_claim_loc.txt"
output_peace_treaties_base = "01_TO_pt_colonial_treaty"
output_scripted_functions = "o_colonial_region_claim_scripted_functions.txt"

jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])

colonial_treaties = [
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_eastern_america",
        "name": "Col. Elysian Coast",
        "full_name": "Colonial Elysian Coast",
        "additional_provinces": [953],
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_louisiana",
        "name": "Colonial Andronika",
        "full_name": "Colonial Andronika & Skythia",
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_california",
        "name": "Colonial Hesperidia",
        "full_name": "Colonial Hesperidia",
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_mexico",
        "name": "Colonial Mexico",
        "full_name": "Colonial Mexico",
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_the_carribean",
        "name": "Col. Kykladian Isles",
        "full_name": "Colonial Kykladian Isles",
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_canada",
        "name": "Colonial Vinland",
        "full_name": "Colonial Vinland",
        "additional_provinces": [980, 997, 994],
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_elysium = yes",
        "region": "colonial_alaska",
        "name": "Colonial Thoulea",
        "full_name": "Colonial Thoulea",
        "base_cost": 20,
        "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_arkadia = yes",
        "region": "colonial_colombia",
        "name": "Colonial Arkadia",
        "full_name": "Colonial Arkadia",
        "base_cost": 20,
        # "cost_reduction_with": "to_cheaper¸_use_pt_colonial_treaties = yes",
        # "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_arkadia = yes",
        "region": "colonial_peru",
        "name": "Colonial Andes",
        "full_name": "Colonial Andes",
        "base_cost": 20,
        # "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        # "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_arkadia = yes",
        "region": "colonial_la_plata",
        "name": "Colonial Parana",
        "full_name": "Colonial Parana",
        "base_cost": 20,
        # "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        # "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_arkadia = yes",
        "region": "colonial_brazil",
        "name": "Colonial Brazil",
        "full_name": "Colonial Brazil",
        "base_cost": 20,
        # "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        # "cost_reduction": 0.5,
    },
    {
        "base_trigger": "to_can_use_pt_colonial_treaties_australia = yes",
        "region": "colonial_australia",
        "name": "Colonial Australia",
        "full_name": "Colonial Australia",
        "base_cost": 20,
        # "cost_reduction_with": "to_cheaper_use_pt_colonial_treaties = yes",
        # "cost_reduction": 0.5,
    },
]

template_peace_treaty = jinja_env.from_string(
    '''
# {{ treaty["full_name"] }}
# For some reason each treaty has to be in its own file...
to_pt_colonial_treaty_{{ treaty["region"] }} = {	
	category = 6
	power_projection = 5
	power_cost_base = 0
	prestige_base = {{ treaty["base_cost"] * 0.0125 }}
	ae_base = 0
	warscore_cost = {
		all_provinces = 0
		no_provinces = {{ treaty["base_cost"] }}
		owner_keeps = 0.0
		conquered = 0.0
		returned_core = 0.0
		released_nation = 0.0
		cancelled_subject = 0.0 
		concede_colonial_region = 0.0
	}
	warscore_cap = {{ treaty["base_cost"] }}
	requires_demand_independence = yes
	is_make_subject = no
	requires_is_allowed = no
	
	is_visible = {
	    # Probably not something that ai should use
	    ai = no
	    
	    {{ treaty["base_trigger"] }}
	    {%- if "cost_reduction_with" in treaty %}
	    NOT = { {{ treaty["cost_reduction_with"] }} }
	    {%- endif %}
		{% if "additional_provinces" in treaty %}
		OR = {
		    {{ treaty["region"] }} = {
				to_country_or_subject_or_subject_of_subject_holds = { TAG = ROOT }
			}
			{%- for province in treaty["additional_provinces"] %}
            {{ province }} = {
                to_country_or_subject_or_subject_of_subject_holds = { TAG = ROOT }
            }
            {%- endfor %}
		}
		{% else %}
		{{ treaty["region"] }} = {
            to_country_or_subject_or_subject_of_subject_holds = { TAG = ROOT }
        }
        {% endif %}
		FROM = {
			OR = {
				NOT = { has_country_flag = to_cannot_colonise_{{ treaty["region"] }} }
				had_country_flag = {
					flag = to_cannot_colonise_{{ treaty["region"] }}
					days = 7300
				}
			}
			NOT = {
				AND = {
					has_country_modifier = nhs2_por_ely_trade
					ROOT = { has_country_modifier = nhs2_ely_por_trade }
				}
			}
			is_subject = no
			num_of_colonists = 1
			NOT = {
				capital_scope = {
				    {% if "cost_reduction_with" in treaty -%}
                    OR = {
                        colonial_region = {{ treaty["region"] }}
                        {%- for province in treaty["additional_provinces"] %}
                        province_id = {{ province }}
                        {%- endfor %}
                    }
                    {% else %}
                    colonial_region = {{ treaty["region"] }}
                    {% endif %}
				}
			}
			{% if "additional_provinces" in treaty %}
            OR = {
                {{ treaty["region"] }} = {
                    is_empty = yes
                    range = FROM
                    OR = {
                        has_port = yes
                        to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
                        any_neighbor_province = {
                            is_colony = no
                            OR = {
                                country_or_subject_holds = FROM
                                owner = {
                                    is_subject = yes
                                    overlord = {
                                        is_subject_of = FROM
                                        NOT = { is_subject_of_type = tributary_state }
                                    }
                                }
                            }
                        }
                    }
                }
                {%- for province in treaty["additional_provinces"] %}
                {{ province }} = {
                    is_empty = yes
                    range = FROM
                    OR = {
                        has_port = yes
                        to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
                        any_neighbor_province = {
                            is_colony = no
                            OR = {
                                country_or_subject_holds = FROM
                                owner = {
                                    is_subject = yes
                                    overlord = {
                                        is_subject_of = FROM
                                        NOT = { is_subject_of_type = tributary_state }
                                    }
                                }
                            }
                        }
                    }
                }
                {%- endfor %}
            }
            {% else %}
            {{ treaty["region"] }} = {
				is_empty = yes
				range = FROM
				OR = {
					has_port = yes
					to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
					any_neighbor_province = {
						is_colony = no
						OR = {
							country_or_subject_holds = FROM
							owner = {
								is_subject = yes
								overlord = {
									is_subject_of = FROM
									NOT = { is_subject_of_type = tributary_state }
								}
							}
						}
					}
				}
			}
            {% endif %}
		}
	}
	is_allowed = {
		always = yes
	}
	effect = {
		FROM = {
			set_country_flag = to_cannot_colonise_{{ treaty["region"] }}
		}
		every_province = {
			limit = {
                {% if "additional_provinces" in treaty %}
                OR = {
                    colonial_region = {{ treaty["region"] }}
                    {%- for province in treaty["additional_provinces"] %}
                    province_id = {{ province }}
                    {%- endfor %}
                }
                {% else %}
                colonial_region = {{ treaty["region"] }}
                {% endif %}
				to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
				is_colony = yes
			}
			add_colonysize = -2000
		}
	}
	ai_weight = {
		export_to_variable = {
			variable_name = ai_value
			value = 0
		}
		limit = {
			always = no
		}
	}
}'''
)

template_peace_treaty_cheaper = jinja_env.from_string(
    '''
# {{ treaty["full_name"] }}, cheaper variant
# For some reason each treaty has to be in its own file...
to_pt_colonial_treaty_{{ treaty["region"] }}_cheaper = {	
	category = 6
	power_projection = 5
	power_cost_base = 0
	prestige_base = {{ (treaty["base_cost"] * 0.0125) / treaty["cost_reduction"] }}
	ae_base = 0
	warscore_cost = {
		all_provinces = 0
		no_provinces = {{ treaty["base_cost"] * treaty["cost_reduction"] }}
		owner_keeps = 0.0
		conquered = 0.0
		returned_core = 0.0
		released_nation = 0.0
		cancelled_subject = 0.0
		concede_colonial_region = 0.0
	}
	warscore_cap = {{ treaty["base_cost"] * treaty["cost_reduction"] }}
	requires_demand_independence = yes
	is_make_subject = no
	requires_is_allowed = no
	
	is_visible = {
	    # Probably not something that ai should use
	    ai = no
	    
		{{ treaty["base_trigger"] }}
		{{ treaty["cost_reduction_with"] }}
		{% if "additional_provinces" in treaty %}
		OR = {
		    {{ treaty["region"] }} = {
				to_country_or_subject_or_subject_of_subject_holds = { TAG = ROOT }
			}
			{%- for province in treaty["additional_provinces"] %}
            {{ province }} = {
                to_country_or_subject_or_subject_of_subject_holds = { TAG = ROOT }
            }
            {%- endfor %}
		}
		{% else %}
		{{ treaty["region"] }} = {
            to_country_or_subject_or_subject_of_subject_holds = { TAG = ROOT }
        }
        {% endif %}
		FROM = {
			OR = {
				NOT = { has_country_flag = to_cannot_colonise_{{ treaty["region"] }} }
				had_country_flag = {
					flag = to_cannot_colonise_{{ treaty["region"] }}
					days = 7300
				}
			}
			NOT = {
				AND = {
					has_country_modifier = nhs2_por_ely_trade
					ROOT = { has_country_modifier = nhs2_ely_por_trade }
				}
			}
			is_subject = no
			num_of_colonists = 1
			NOT = {
				capital_scope = {
				    {% if "cost_reduction_with" in treaty -%}
                    OR = {
                        colonial_region = {{ treaty["region"] }}
                        {%- for province in treaty["additional_provinces"] %}
                        province_id = {{ province }}
                        {%- endfor %}
                    }
                    {% else %}
                    colonial_region = {{ treaty["region"] }}
                    {% endif %}
				}
			}
			{% if "additional_provinces" in treaty %}
            OR = {
                {{ treaty["region"] }} = {
                    is_empty = yes
                    range = FROM
                    OR = {
                        has_port = yes
                        to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
                        any_neighbor_province = {
                            is_colony = no
                            OR = {
                                country_or_subject_holds = FROM
                                owner = {
                                    is_subject = yes
                                    overlord = {
                                        is_subject_of = FROM
                                        NOT = { is_subject_of_type = tributary_state }
                                    }
                                }
                            }
                        }
                    }
                }
                {%- for province in treaty["additional_provinces"] %}
                {{ province }} = {
                    is_empty = yes
                    range = FROM
                    OR = {
                        has_port = yes
                        to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
                        any_neighbor_province = {
                            is_colony = no
                            OR = {
                                country_or_subject_holds = FROM
                                owner = {
                                    is_subject = yes
                                    overlord = {
                                        is_subject_of = FROM
                                        NOT = { is_subject_of_type = tributary_state }
                                    }
                                }
                            }
                        }
                    }
                }
                {%- endfor %}
            }
            {% else %}
            {{ treaty["region"] }} = {
				is_empty = yes
				range = FROM
				OR = {
					has_port = yes
					to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
					any_neighbor_province = {
						is_colony = no
						OR = {
							country_or_subject_holds = FROM
							owner = {
								is_subject = yes
								overlord = {
									is_subject_of = FROM
									NOT = { is_subject_of_type = tributary_state }
								}
							}
						}
					}
				}
			}
            {% endif %}
		}
	}
	is_allowed = {
		always = yes
	}
	effect = {
		FROM = {
			set_country_flag = to_cannot_colonise_{{ treaty["region"] }}
		}
		every_province = {
			limit = {
                {% if "additional_provinces" in treaty %}
                OR = {
                    colonial_region = {{ treaty["region"] }}
                    {%- for province in treaty["additional_provinces"] %}
                    province_id = {{ province }}
                    {%- endfor %}
                }
                {% else %}
                colonial_region = {{ treaty["region"] }}
                {% endif %}
				to_country_or_subject_or_subject_of_subject_holds = { TAG = FROM }
				is_colony = yes
			}
			add_colonysize = -2000
		}
	}
	ai_weight = {
		export_to_variable = {
			variable_name = ai_value
			value = 0
		}
		limit = {
			always = no
		}
	}
}''')

template_scripted_functions = jinja_env.from_string(
    '''{%- for treaty in colonial_treaties %}    condition = {
		tooltip = "TO_COLONIAL_TREATY"
		potential = {
			colonial_region = {{ treaty['region'] }}
			FROM = {
			    to_has_or_overlord_has_claim_colonial_region_peace_treaty = {
			        COLONIAL_REGION = {{ treaty['region'] }}
			    }
			}
		}
		allow = {
			always = no
		}
	}
{% endfor %}    # End of code gen. segment''')

template_loc = jinja_env.from_string(
    "{% for treaty in colonial_treaties %}"
    " to_pt_colonial_treaty_{{ treaty['region'] }}_desc:0 \""
    "Prevents [From.GetName] and its Subjects from colonizing in §Y{{ treaty['full_name'] }}§! for the next §Y20§! "
    "years. All their unfinished colonies in the region will be §Rabandoned§!.\"\n"
    " CB_ALLOWED_to_pt_colonial_treaty_{{ treaty['region'] }}:0 \"Claim {{ treaty['name'] }}\"\n"
    " PEACE_to_pt_colonial_treaty_{{ treaty['region'] }}:0 \"§YClaim {{ treaty['name'] }}§!\"\n"
    "{% if 'cost_reduction_with' in treaty %}"
    " to_pt_colonial_treaty_{{ treaty['region'] }}_cheaper_desc:0 \""
    "Prevents [From.GetName] and its Subjects from colonizing in §Y{{ treaty['full_name'] }}§! for the next §Y20§! "
    "years. All their unfinished colonies in the region will be §Rabandoned§!.\"\n"
    " CB_ALLOWED_to_pt_colonial_treaty_{{ treaty['region'] }}_cheaper:0 \"Claim {{ treaty['name'] }}\"\n"
    " PEACE_to_pt_colonial_treaty_{{ treaty['region'] }}_cheaper:0 \"§YClaim {{ treaty['name'] }}§!\"\n"
    "{% endif %}"
    "{% endfor %}"
)

for treaty in colonial_treaties:
    path = os.path.join(output_peace_treaties, f"{output_peace_treaties_base}_{treaty['region']}.txt")
    f = open(path, "w")
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}")
    f.write(template_peace_treaty.render(treaty=treaty))
    f.close()
    if "cost_reduction_with" in treaty:
        path = os.path.join(output_peace_treaties, f"{output_peace_treaties_base}_{treaty['region']}_cheaper.txt")
        f = open(path, "w")
        f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}")
        f.write(template_peace_treaty_cheaper.render(treaty=treaty))
        f.close()

f = open(output_loc, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write(template_loc.render(colonial_treaties=colonial_treaties))
f.close()

f = open(output_scripted_functions, "w")
f.write(f"    # Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write(template_scripted_functions.render(colonial_treaties=colonial_treaties))
f.close()