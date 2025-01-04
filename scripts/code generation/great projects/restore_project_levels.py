import json


def write_line(file, line: str, indent: int = 0):
    file.write("\t" * indent)
    file.write(line)
    file.write("\n")


with open("monuments.json") as i:
    great_project_names = json.load(i)

with open("output_save.txt", "w") as o:
    write_line(o, "to_save_great_project_levels = {")
    for i, great_project in enumerate(great_project_names):
        write_line(o, "if = {", 1)
        write_line(o, f"limit = {{ has_great_project = {{ type = {great_project} tier = 0 }} }}", 2)
        for tier in range(3, 0, -1):
            if tier == 3:
                write_line(o, "if = {", 2)
            else:
                write_line(o, "else_if = {", 2)
            write_line(o, f"limit = {{ has_great_project = {{ type = {great_project} tier = {tier} }} }}", 3)
            write_line(o, f"set_province_flag = to_had_great_project_{great_project}_tier_{tier}", 3)
            write_line(o, "}", 2)
        write_line(o, "else = {", 2)
        write_line(o, f"set_province_flag = to_had_great_project_{great_project}_tier_0", 3)
        write_line(o, "}", 2)
        write_line(o, "}", 1)
    write_line(o, "}")

with open("output_load.txt", "w") as o:
    write_line(o, "to_load_great_project_levels = {")
    for i, great_project in enumerate(great_project_names):
        write_line(o, "if = {", 1)
        write_line(o, f"limit = {{ has_great_project = {{ type = {great_project} tier = 0 }} }}", 2)
        for tier in range(3, -1, -1):
            # if tier == 3:
            #     write_line(o, "if = {", 2)
            # else:
            #     write_line(o, "else_if = {", 2)
            write_line(o, "if = {", 2)
            write_line(o, f"limit = {{ has_province_flag = to_had_great_project_{great_project}_tier_{tier} }}", 3)
            write_line(o, f"clr_province_flag = to_had_great_project_{great_project}_tier_{tier}", 3)
            # for tier_current in range(3, -1, -1):
            #     if tier_current == 3:
            #         write_line(o, "if = {", 3)
            #     else:
            #         write_line(o, "else_if = {", 3)
            #     write_line(o, f"limit = {{ has_great_project = {{ type = {great_project} tier = {tier_current} }} }}", 4)
            #     if tier != tier_current:
            #         write_line(o, f"add_great_project_tier = {{ type = {great_project} tier = {tier - tier_current} }}", 4)
            #     write_line(o, "}", 3)
            for tier_current in range(3, -1, -1):
                if tier == tier_current:
                    continue
                write_line(o, "if = {", 3)
                write_line(o, "limit = {", 4)
                write_line(o, f"has_great_project = {{ type = {great_project} tier = {tier_current} }}", 5)
                if tier_current < 3:
                    write_line(o, f"NOT = {{ has_great_project = {{ type = {great_project} tier = {tier_current + 1} }} }}", 5)
                write_line(o, "}", 4)
                write_line(o, f"add_great_project_tier = {{ type = {great_project} tier = {tier - tier_current} }}", 4)
                write_line(o, "}", 3)
            write_line(o, "}", 2)
        write_line(o, "}", 1)
    write_line(o, "}")
