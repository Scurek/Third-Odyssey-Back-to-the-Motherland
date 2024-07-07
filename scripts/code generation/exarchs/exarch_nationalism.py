import os


def btree_triplet(lst, form, body):
    if not len(lst):
        return ''
    elif len(lst) == 1:
        return body % (lst[0][1], lst[0][2])
    else:
        return form % (lst[int(len(lst) / 2)][0],
                       btree_triplet(lst[int(len(lst) / 2):], form, body),
                       btree_triplet(lst[:int(len(lst) / 2)], form, body))

MIN_MODIFIER = -50
MAX_MODIFIER = 50


cond = 'check_variable={which=to_exarch_nationalism_diff value=%s}'
body = 'if = {limit={NOT={has_country_modifier=to_exarch_nationalism_%s}} ' \
       'to_remove_exarch_nationalism_modifiers=yes add_country_modifier={' \
       'name=to_exarch_nationalism_%s duration=-1 hidden = yes} }'
form = 'if={limit={%s}%s}else={%s}' % (cond, '%s', '%s')


def btree(lst, form, body):
    if not len(lst):
        return ''
    elif len(lst) == 1:
        return body % (lst[0], lst[0])
    else:
        return form % (lst[int(len(lst) / 2)],
                       btree(lst[int(len(lst) / 2):], form, body),
                       btree(lst[:int(len(lst) / 2)], form, body))

MAX_LOCAL_MODIFIER = 100

cond_local = 'check_variable={which=to_saved_years_of_nationalism value=%s}'
body_local = 'if = {limit={NOT={has_province_modifier=to_exarch_local_nationalism_%s}} ' \
       'add_province_modifier={' \
       'name=to_exarch_local_nationalism_%s duration=-1 hidden = yes} }'
form_local = 'if={limit={%s}%s}else={%s}' % (cond_local, '%s', '%s')


with open('o_exarch_nationalism_effects.txt', 'w') as f:
    f.write('to_remove_exarch_nationalism_modifiers = {\n')
    f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(MIN_MODIFIER, MAX_MODIFIER + 1):
        f.write(f"	remove_country_modifier = to_exarch_nationalism_{i + abs(MIN_MODIFIER)}\n")
    f.write("}\n\n")

    f.write('to_add_correct_exarch_nationalism_modifier = {\n')
    f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n	")
    f.write(btree_triplet([(i, i + abs(MIN_MODIFIER), i + abs(MIN_MODIFIER)) for i in range(MIN_MODIFIER, MAX_MODIFIER + 1)], form, body))
    f.write("\n}\n\n")

    # LOCAL
    f.write('to_remove_exarch_local_nationalism_modifiers = {\n')
    f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(1, MAX_LOCAL_MODIFIER + 1):
        f.write(f"	remove_province_modifier = to_exarch_local_nationalism_{i}\n")
    f.write("}\n\n")

    f.write('to_add_correct_exarch_local_nationalism_modifier = {\n')
    f.write(f"	# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n	")
    f.write(btree(
        [i for i in range(1, MAX_LOCAL_MODIFIER + 1)], form_local,
        body_local) + '\n}')

with open('o_exarch_nationalism_modifiers.txt', 'w') as f:
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(MIN_MODIFIER, MAX_MODIFIER + 1):
        f.write(f"to_exarch_nationalism_{i + abs(MIN_MODIFIER)} = {{\n")
        f.write(f"	years_of_nationalism = {i}\n")
        f.write("}\n")
    # LOCAL
    for i in range(1, MAX_LOCAL_MODIFIER + 1):
        f.write(f"to_exarch_local_nationalism_{i} = {{\n")
        f.write(f"	local_years_of_nationalism = {i}\n")
        f.write("}\n")

with open('o_exarch_nationalism_localisation.txt', 'w') as f:
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(MIN_MODIFIER, MAX_MODIFIER + 1):
        f.write(f" to_exarch_nationalism_{i + abs(MIN_MODIFIER)}:0 \"Overlord's Years of Separatism Difference\"\n")