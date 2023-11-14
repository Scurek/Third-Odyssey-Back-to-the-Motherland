import os

def btree(lst, form, body):
    if   len(lst):
        return ''
    elif len(lst) == 1:
        return body % (lst[0], lst[0])
    else:
        return form % (lst[int(len(lst) / 2)],
                       btree(lst[int(len(lst) / 2):], form, body),
                       btree(lst[:int(len(lst) / 2)], form, body))

def btree1arg(lst, form, body):
    if not len(lst):
        return ''
    elif len(lst) == 1:
        return body % (lst[0])
    else:
        return form % (lst[int(len(lst) / 2)],
                       btree1arg(lst[int(len(lst) / 2):], form, body),
                       btree1arg(lst[:int(len(lst) / 2)], form, body))

def btree_tuple(lst, form, body):
    if not len(lst):
        return ''
    elif len(lst) == 1:
        return body % (lst[0][0], lst[0][1])
    else:
        return form % (lst[int(len(lst) / 2)][0],
                       btree_tuple(lst[int(len(lst) / 2):], form, body),
                       btree_tuple(lst[:int(len(lst) / 2)], form, body))

MAX_MODIFIER = 10

MAX_COST = 100
MIN_COST = 50
INTERVALS = 10

cond = 'check_variable={which=$VARIABLE$ value=%s}'
body = 'if = {limit={NOT={has_country_modifier=$MODIFIER_BASE$_%s}} ' \
       'to_remove_ab_penalty_modifiers={ MODIFIER_BASE = $MODIFIER_BASE$ } add_country_modifier={' \
       'name=$MODIFIER_BASE$_%s duration=-1 hidden = yes} }'
form = 'if={limit={%s}%s}else={%s}' % (cond, '%s', '%s')

cond_corr = 'has_government_power={mechanic_type = to_administrative_burden_mechanic power_type = ' \
            'to_administrative_burden value=%s }'
body_corr = 'custom_tooltip=to_add_administrative_burden_corruption_%s_tt hidden_effect={add_corruption=%s}'
form_corr = 'if={limit={%s}%s}else={%s}' % (cond_corr, '%s', '%s')

MAX_BURDEN = 30

with open('o_scripted_effects.txt', 'w') as f:
    f.write('to_set_administrative_burden_penalty = {\n')
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    f.write(btree([i for i in range(1, MAX_MODIFIER + 1)], form, body) + '\n}')
    f.write("\n\n")
    f.write('to_remove_ab_penalty_modifiers = {\n')
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(1, MAX_MODIFIER + 1):
        f.write(f'\tremove_country_modifier = $MODIFIER_BASE$_{i}\n')
    f.write('}')
    f.write("\n\n")
    f.write('to_add_corruption_from_administrative_burden = {\n')
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    f.write(btree_tuple([(i, (i-5)/2) for i in range(7, MAX_BURDEN + 1, 2)], form_corr, body_corr) + '\n}')

with open('o_event_modifiers.txt', 'w') as f:
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(1, MAX_MODIFIER + 1):
        f.write(f'to_ab_subject_penalty_mod_{i} = {{ \n')
        f.write(f'\tmonthly_to_administrative_burden = {0.15 * i:.2f}\n')
        f.write('}\n')
    for i in range(1, MAX_MODIFIER + 1):
        f.write(f'to_ab_colony_penalty_mod_{i} = {{ \n')
        f.write(f'\tmonthly_to_administrative_burden = {0.05 * i:.2f}\n')
        f.write('}\n')

with open('o_localisation.txt', 'w') as f:
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i in range(1, MAX_MODIFIER + 1):
        f.write(f' to_ab_subject_penalty_mod_{i}:0 "Disloyal Subjects"\n')
    for i in range(1, MAX_MODIFIER + 1):
        f.write(f' to_ab_colony_penalty_mod_{i}:0 "Active Colonies"\n')
    for i in range(7, MAX_BURDEN + 1, 2):
        f.write(f' to_add_administrative_burden_corruption_{i}_tt:0 "Gain §R{(i - 5) / 2}0§! Corruption from excess '
                f'§YAdministrative Burden§!."\n')

cond_adm = 'check_variable={which=to_ab_expand_bureaucracy_cost value=%s}'
body_adm = 'adm_power=%s'
form_adm = 'if={limit={%s}%s}else={%s}' % (cond_adm, '%s', '%s')
with open('o_scripted_triggers.txt', 'w') as f:
    f.write('to_ab_can_expand_bureaucracy_adm = {\n')
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    f.write(btree1arg([i for i in range(MIN_COST, MAX_COST + 1, INTERVALS)], form_adm, body_adm))
    f.write('\n}')