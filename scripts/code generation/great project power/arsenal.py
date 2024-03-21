import os

MAX_PRODUCTION = 50
MAX_PRODUCTION_NON_DLC = 40
STEPS = 10

SHIP_COST_MOD = 0.30
ARTILLERY_MAIN_MOD = 0.10

output_file_cm = "o_conditional_modifiers.txt"
output_file_upgrade_effect = "o_upgrade_effects.txt"
output_file_localisation = "o_localisation.txt"
output_file_frames = "o_frames.txt"

dlc_step = MAX_PRODUCTION // STEPS
non_dlc_step = MAX_PRODUCTION_NON_DLC // STEPS

with open(output_file_cm, 'w') as f:
    f.write(f"\t\t# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    dlc_production = range(dlc_step, MAX_PRODUCTION + 1, dlc_step)
    non_dlc_production = range(non_dlc_step, MAX_PRODUCTION_NON_DLC + 1, non_dlc_step)

    for dlc_prod, non_dlc_prod in zip(dlc_production, non_dlc_production):
        perc = dlc_prod / MAX_PRODUCTION
        ship_cost = round(perc * SHIP_COST_MOD, 2)
        arty_maintenance = round(perc * ARTILLERY_MAIN_MOD, 2)
        f.write("\t\tconditional_modifier = {\n")
        f.write("\t\t\ttooltip_potential = { always = no }\n")
        f.write("\t\t\ttrigger = {\n")

        f.write(f"\t\t\t\tif = {{ limit = {{ has_dlc = \"Mandate of Heaven\" }}\n")
        f.write(f"\t\t\t\t\ttrade_goods_produced_amount = {{ trade_goods = naval_supplies amount = {dlc_prod} }}\n")
        if dlc_prod != MAX_PRODUCTION:
            f.write(
                f"\t\t\t\t\tNOT = {{ trade_goods_produced_amount = {{ "
                f"trade_goods = naval_supplies amount = {dlc_prod + dlc_step} }} }}\n")
        f.write(f"\t\t\t\t}}\n")
        f.write(f"\t\t\t\telse = {{\n")
        f.write(f"\t\t\t\t\ttrade_goods_produced_amount = {{ trade_goods = naval_supplies amount = {non_dlc_prod} }}\n")
        if dlc_prod != MAX_PRODUCTION:
            f.write(
                f"\t\t\t\t\tNOT = {{ trade_goods_produced_amount = {{ "
                f"trade_goods = naval_supplies amount = {non_dlc_prod + non_dlc_step} }} }}\n")
        f.write(f"\t\t\t\t}}\n")

        f.write("\t\t\t}\n")
        if dlc_prod != MAX_PRODUCTION:
            f.write(f"\t\t\tmodifier = {{ global_ship_cost = -{ship_cost} artillery_cost = -{arty_maintenance} }}\n")
        else:
            f.write(f"\t\t\tmodifier = {{\n"
                    f"\t\t\t\tglobal_ship_cost = -{ship_cost}\n"
                    f"\t\t\t\tartillery_cost = -{arty_maintenance}\n"
                    f"\t\t\t\tnumber_of_cannons_modifier = 0.1\n"
                    f"\t\t\t\tmax_flagships = 1\n"
                    f"\t\t\t}}\n")
        f.write("\t\t}\n")
        f.write("\n")

with open(output_file_upgrade_effect, 'w') as f:
    dlc_production = range(MAX_PRODUCTION, -1, -dlc_step)
    non_dlc_production = range(MAX_PRODUCTION_NON_DLC, -1, -non_dlc_step)

    f.write(f"\t# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    for i, prod in enumerate(zip(dlc_production, non_dlc_production)):
        dlc_prod, non_dlc_prod = prod
        perc = dlc_prod / MAX_PRODUCTION
        ship_cost = round(perc * SHIP_COST_MOD, 2)
        arty_maintenance = round(perc * ARTILLERY_MAIN_MOD, 2)
        if i == 0:
            f.write("\tif = {\n")
        elif dlc_prod != 0:
            f.write("\telse_if = {\n")
        else:
            f.write("\telse = {\n")
        if dlc_prod != 0:
            f.write("\t\tlimit = {\n")
            f.write(f"\t\t\tto_owner_has_naval_supplies_production = {{ VALUE = {dlc_prod} NON_DLC_VALUE = {non_dlc_prod} }}\n")
            f.write("\t\t}\n")
        f.write(f"\t\tcustom_tooltip = to_arsenal_power_effect_{round(100 * perc)}_tt\n")
        f.write("\t}\n")

with open(output_file_localisation, 'w') as f:
    f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")

    dlc_production = range(0, MAX_PRODUCTION + 1, dlc_step)
    non_dlc_production = range(0, MAX_PRODUCTION_NON_DLC + 1, non_dlc_step)

    for dlc_prod, non_dlc_prod in zip(dlc_production, non_dlc_production):
        perc = dlc_prod / MAX_PRODUCTION
        ship_cost = round(perc * SHIP_COST_MOD, 2)
        arty_maintenance = round(perc * ARTILLERY_MAIN_MOD, 2)
        color = "G"
        if dlc_prod == 0:
            color = "Y"
        f.write(f" to_arsenal_power_effect_{round(100 * perc)}_tt:0 \"\\n"
                f"Ship Cost: §{color}-{100 * ship_cost:.1f}%§! from §YArsenal Efficiency§!\\n"
                f"Artillery Cost: §{color}-{100 * arty_maintenance:.1f}%§! from §YArsenal Efficiency§!")
        if dlc_prod == MAX_PRODUCTION:
            f.write(f"\\nShip Cannons §G+10.0%§! from §YArsenal Efficiency§!"
                    f"[AdditionalFlagshipFromArsenal]")
        f.write(f"\"\n")

with open(output_file_frames, 'w') as f:
    f.write(f"\t# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    dlc_production = range(MAX_PRODUCTION, 1, -dlc_step)
    non_dlc_production = range(MAX_PRODUCTION_NON_DLC, 1, -non_dlc_step)

    for dlc_prod, non_dlc_prod in zip(dlc_production, non_dlc_production):
        perc = dlc_prod / MAX_PRODUCTION
        display_perc = int(100 * perc)
        ship_cost = round(perc * SHIP_COST_MOD, 2)
        arty_maintenance = round(perc * ARTILLERY_MAIN_MOD, 2)
        f.write("\tframe = {\n")
        f.write(f"\t\tnumber = {display_perc}\n")
        f.write("\t\ttrigger = { ")
        f.write(f"to_owner_has_naval_supplies_production = {{ VALUE = {dlc_prod} NON_DLC_VALUE = {non_dlc_prod} }}")
        f.write(" }\n")
        f.write("\t}\n")