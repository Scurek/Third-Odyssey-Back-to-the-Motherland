import os

from exarchs import exarchs

output_file = "o_exarch_name_from_province.txt"

f = open(output_file, "w", encoding="utf-8")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for exarch in exarchs:
    f.write(f"	text = {{\n"
            f"		localisation_key = to_{exarch['tag']}_name_tt\n"
            f"		trigger = {{ nhs_{exarch['tag']}_province = yes }}\n"
            f"	}}\n")
    # if "subtags" not in exarch:
    #     f.write(f"	text = {{\n"
    #             f"		localisation_key = {exarch['tag']}\n"
    #             f"		trigger = {{ nhs_{exarch['tag']}_province = yes }}\n"
    #             f"	}}\n")
    # else:
    #     for subtag in exarch["subtags"]:
    #         f.write(f"	text = {{\n"
    #                 f"		localisation_key = {exarch['tag']}\n"
    #                 f"		trigger = {{ {exarch['reference_target']} = {{ tag = {subtag} }} "
    #                 f"nhs_{exarch['tag']}_province = yes }}\n"
    #                 f"	}}\n")
f.close()

output_file = "o_scripted_effects.txt"
f = open(output_file, "w", encoding="utf-8")
f.write("to_exarch_effect = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for exarch in exarchs:
    f.write(f"	if = {{\n"
            f"		limit = {{ exists = {exarch['reference_target']} }}\n"
            f"		{exarch['reference_target']} = {{ $EFFECT$ }}\n"
            f"	}}\n")
f.write("}\n\n")

f.write("to_exarch_effect_including_inactive = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for exarch in exarchs:
    f.write(f"	{exarch['reference_target']} = {{ $EFFECT$ }}\n")
f.write("}\n\n")

f.write("to_exarch_effect_from_province = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for i in range(len(exarchs)):
    exarch = exarchs[i]
    if i == 0:
        f.write(f"	if = {{\n")
    else:
        f.write(f"	else_if = {{\n")
    f.write(f"		limit = {{ nhs_{exarch['tag']}_province = yes }}\n"
            f"		{exarch['reference_target']} = {{ $EFFECT$ }}\n"
            f"	}}\n")
f.write("}\n\n")

f.write("to_change_tag_to_local_exarch = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for i in range(len(exarchs)):
    exarch = exarchs[i]
    if i == 0:
        f.write(f"	if = {{\n")
    else:
        f.write(f"	else_if = {{\n")
    f.write(f"		limit = {{ capital_scope = {{ nhs_{exarch['tag']}_province = yes }} }}\n"
            f"		to_change_tag = {{ TAG =  {exarch['tag']} }}\n"
            f"	}}\n")
f.write("}")
f.close()

output_file = "o_scripted_triggers.txt"
f = open(output_file, "w", encoding="utf-8")

# f.write("to_potential_exarch_province = {\n")
# f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
# f.write(f"	OR = {{\n")
# for exarch in exarchs:
#     f.write(f"		nhs_{exarch['tag']}_province = yes\n")
# f.write(f"	}}\n")
# f.write("}\n\n")

# f.write("to_is_exarch = {\n")
# f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
# f.write(f"	OR = {{\n")
# for exarch in exarchs:
#     f.write(f"		tag = {exarch['reference_target']}\n")
# f.write(f"	}}\n")
# f.write("}\n\n")

f.write("to_exarch_land = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write(f"	OR = {{\n")
for exarch in exarchs:
    f.write(f"		AND = {{\n"
            f"			$SCOPE$ = {{ tag = {exarch['reference_target']} }}\n"
            f"			nhs_{exarch['tag']}_province = yes\n"
            f"		}}\n")
f.write(f"	}}\n")
f.write("}\n\n")

f.write("to_exarch_trigger_from_province = {\n")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write("	if = {\n"
        "		limit = { owner = { is_subject_of_type = elysian_subject } }\n"
        "		owner = { $TRIGGER$ }\n"
        "	}\n")
for exarch in exarchs:
    f.write(f"	else_if = {{\n")

    f.write(f"		limit = {{ nhs_{exarch["tag"]}_province = yes }}\n"
            f"		{exarch["reference_target"]} = {{ $TRIGGER$ }}\n"
            f"	}}\n")
f.write("}\n\n")

f.close()



output_file = "o_send_aid_modifiers.txt"
f = open(output_file, "w", encoding="utf-8")
f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for i in range(1, 17):
    f.write(f"	modifier_overlord = {{\n"
            f"		trigger = {{ has_country_modifier = to_exarch_aid check_variable = {{ which = to_exarch_send_aid_cost value = {i} }} }}\n"
            f"		modifier = to_exarch_aid_penalty_{i}\n"
            f"	}}\n")
f.write("\n")
f.close()

output_file = "o_static_modifier.txt"
f = open(output_file, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for i in range(1, 17):
    f.write(f"to_exarch_aid_penalty_{i} = {{\n"
            f"	global_tax_income = {-12}\n"
            f"}}\n")
f.write("\n")
f.close()

output_file = "TO_exarchs_revolt_triggers.txt"
f = open(output_file, "w", encoding="utf-8")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
for exarch in exarchs:
    f.write(f"{exarch["tag"]} = {{ exists = {exarch["tag"]} }}\n")
    if "subtags" in exarch:
        for subtag in exarch["subtags"]:
            f.write(f"{subtag} = {{ exists = {subtag} }}\n")
f.close()