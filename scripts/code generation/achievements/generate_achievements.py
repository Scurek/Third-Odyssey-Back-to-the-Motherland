import json
import os

gui_file = open("TO_achievements.txt", "w")
loc_file = open("to_achievement_localisation.txt", "w", encoding="utf-8")
interface_file = open("to_achievement_interface.txt", "w")
completion_file = open("to_achievement_completion.txt", "w")
gfx_file = open("z_TO_achievements.gfx", "w")
cl_file = open("TO_ANY_achievements_customizable_localization.txt", "w")
events_file = open("to_achievement_events.txt", "w")
scripted_triggers_file = open("to_achievement_scripted_triggers.txt", "w")
scripted_effects_file = open("to_achievement_scripted_effects.txt", "w")

window_gui = """custom_window = {
\tname = to_achievement_window
\tpotential = {
\t\tto_achievement_window_visible = yes
\t}
}

custom_button = {
\tname = to_achievements_button_open
\ttooltip = to_achievements_button_open_tooltip
\ttrigger = {
\t\tto_has_achievements = yes
\t}
\teffect = {
\t\tif = {
\t\t\tlimit = { has_country_flag = to_achievement_window_open }
\t\t\tclr_country_flag = to_achievement_window_open
\t\t}
\t\telse = {
\t\t\tset_country_flag = to_achievement_window_open
\t\t}
\t}
}

custom_button = {
\tname = to_achievement_close_button
\teffect = {
\t\tclr_country_flag = to_achievement_window_open
\t}
}

custom_window = {
\tname = to_achievement_window_elysia
\tpotential = {
\t\tto_has_elysian_achievements = yes
\t}
}

custom_window = {
\tname = to_show_achievements
\tpotential = {
\t\tto_show_achievements = yes
\t}
}

custom_text_box = {
\tname = to_achievements_old_patch
\tpotential = {
\t\tNOT = { to_show_achievements = yes }
\t}
}

custom_window = {
\tname = to_achievement_ironman_error
\tpotential = {
\t\tironman = no
\t}
}

# Unused, but if those aren't here error.log keeps throwing false positive errors. Thanks Paradox.
custom_button = {
\tname = to_achievement_elysia_title
}
custom_button = {
\tname = to_ironman_error_not_enabled
}
################

custom_text_box = {
\tname = to_ironman_error_not_enabled
}


custom_text_box = {
\tname = to_achievement_elysia_title
}

custom_text_box = {
\tname = to_achievement_completed
}

custom_text_box = {
\tname = to_achievement_completed_close_text
}

"""

window_interface = """\t\twindowType = {
\t\t\tname = "to_achievement_window"
\t\t\tposition = { x = 0 y = 0 }
\t\t\tOrientation = "CENTER"
\t\t\tscripted = yes
    
\t\t\twindowType = {
\t\t\t\tname = "to_achievement_window"
\t\t\t\tposition = { x = 0 y = 0 }
\t\t\t\tOrientation = "CENTER"
\t\t\t\tscripted = yes

"""

gfx_entries = """\tspriteType = {
\t\tname = "GFX_to_achievement_entry_easy"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_entry_easy.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_entry_medium"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_entry_medium.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_entry_hard"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_entry_hard.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_status_background"
\t\ttexturefile = "gfx//interface//TO_achievements//status_background.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_status_icons"
\t\ttexturefile = "gfx//interface//TO_achievements//status_icons.dds"
\t\tnoOfFrames = 3
\t}

\tspriteType = {
\t\tname = "GFX_to_province_decision_button"
\t\ttexturefile = "gfx//interface//TO_achievements//province_decision_button.dds"
\t}

\tframeAnimatedSpriteType = {
\t\tname = "GFX_to_province_decision_button_highlight"
\t\ttexturefile = "gfx//interface//TO_achievements//province_decision_button_highlight.dds"
\t\tnoOfFrames = 40
\t\ttransparencecheck = yes
\t\tanimation_rate_fps = 20
\t\tlooping = yes
\t\tplay_on_show = yes
\t\talwaystransparent = yes
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_completed_window_easy"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_complete_window_easy.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_completed_window_medium"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_complete_window_medium.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_completed_window_hard"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_complete_window_hard.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_ironman_error_bg"
\t\ttexturefile = "gfx//interface//TO_achievements//ironman_error_bg.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_no_ironman_icon"
\t\ttexturefile = "gfx//interface//TO_achievements//no_ironman_icon.dds"
\t}

\tspriteType = {
\t\tname = "GFX_achievement_complete_image_frame"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_complete_image_frame.dds"
\t}

\tspriteType = {
\t\tname = "GFX_achievement_complete_image_frame_133x133"
\t\ttexturefile = "gfx//interface//TO_achievements//achievement_complete_image_frame_133x133.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_button_achievements_elysia"
\t\ttexturefile = "gfx//interface//TO_achievements//button_achievements_elysia.dds"
\t}

\tspriteType = {
\t\tname = "GFX_to_achievement_background_elysia"
\t\ttexturefile = "gfx//interface//TO_achievements//background_elysia_large.dds"
\t}

"""

# cl_entries = """defined_text = {
#     name = ToAchievements_to_did_not_start_on_ironman
#     random = no
#     text = {
#         localisation_key = to_red_y_icon_tt
#         trigger = {
#             to_did_not_start_on_ironman = yes
#         }
#     }
#     text = {
#         localisation_key = to_green_x_icon_tt
#     }
# }
#
# """
cl_entries = """defined_text = {
    name = ToAchievements_checkIronman
    random = no
    text = {
        localisation_key = to_achievement_warning_ironman_tt
        trigger = {
            ironman = no
        }
    }
    text = {
        localisation_key = to_empty_string_tt
    }
}

"""

y_spacing = 87
x_spacing = 358  #383
top_margin = 108
left_margin = 12

icon_offset_x = 7
icon_offset_y = 6

status_background_offset_x = 292
status_background_offset_y = 22
status_background_offset_x_low_diff = 0
status_background_offset_y_low_diff = 14

status_offset_x = 300
status_offset_y = 22
status_offset_x_low_diff = 0
status_offset_y_low_diff = 14

province_decision_offset_x = 316
province_decision_offset_y = 8

title_offset_x = 82
title_offset_y = 8
title_width = 185
title_font = "vic_22"

description_offset_x = 82
description_offset_y = 30
description_width = 200
description_font = "vic_18"

completed_icon_offset_x = 154
completed_icon_offset_y = 145

completed_title_text_offset_x = 135
completed_title_text_offset_y = 99
completed_title_text_font = "vic_22"
completed_title_text_width = 270

completed_title_offset_x = 100
completed_title_offset_y = 120
completed_title_font = "vic_18"
completed_title_width = 330

completed_description_offset_x = 63
completed_description_offset_y = 296
completed_description_font = "vic_18"
completed_description_width = 400
completed_description_height = 83

completed_score_offset_x = 65
completed_score_offset_y = 347
completed_score_font = "vic_18"
completed_score_width = 400

completed_close_offset_x = 210
completed_close_offset_y = 387

completed_close_text_offset_x = 235
completed_close_text_offset_y = 393
completed_close_text_font = "vic_18"
completed_close_text_width = 60

events_starting_id = 100
events_namespace = "to_achievements"

fail_conditions_intro = "\\n§RWe will no longer be able to complete the achievement if any of the following is true:§!\\n"


def has_province_decision(achievement):
    return "has_province_decision" in achievement and achievement["has_province_decision"]


def condition_only_shown_when_true(condition):
    if "only_shown_when_true" in condition and condition["only_shown_when_true"]:
        return True
    return False


def has_always_visible_fail_condition(fail_conditions):
    for fail_condition in fail_conditions:
        if not condition_only_shown_when_true(fail_condition):
            return True
    return False


def has_development_score(entry):
    return "score" in entry and entry["score"] == "development"


loc_entries_added = set()
cl_entries_added = set()

with open("achievement_definitions.json") as file:
    data = json.load(file)
    loc_file.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    loc_file.write(f" to_achievements_fail_condition_intro_tt:0 \"{fail_conditions_intro}\"\n")
    gui_file.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    gui_file.write(window_gui)
    # interface_file.write(f"\t\t# Third Odyssey\n")
    interface_file.write(
        f"\t\t\t\t\t# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    completion_file.write(
        f"\t\t# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    # interface_file.write(window_interface)
    gfx_file.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    gfx_file.write("spriteTypes = {\n")
    gfx_file.write(gfx_entries)
    cl_file.write(cl_entries)
    events_file.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    scripted_triggers_file.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
    scripted_effects_file.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")

    scripted_effects_file.write("transfer_achievement_completion = {\n")
    for entry in data:
        if "removed" in entry:
            continue
        scripted_effects_file.write(f"\tif = {{\n"
                                    f"\t\tlimit = {{ $ORIGIN$ = {{ to_achievement_status_completed = {{ ACHIEVEMENT = {entry["name"]} }} }} }}\n"
                                    f"\t\t$TARGET$ = {{ to_set_achievement_completed_flag = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                                    f"\t}}\n")
    scripted_effects_file.write("}\n\n")

    true_index = -1

    for entry in data:
        if "removed" in entry:
            continue
        true_index += 1
        # gui_file.write(f"custom_icon = {{\n"
        #                f"\tname = to_achievement_{entry["name"]}_icon\n"
        #                f"}}\n\n")

        # Attempt to fix error.log
        gui_file.write("# Unused, but if those aren't here error.log keeps throwing false positive errors. "
                       "Thanks Paradox.\n")
        gui_file.write(f"custom_button = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_title\n"
                       f"}}\n\n")
        gui_file.write(f"custom_button = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_background\n"
                       f"\ttooltip = to_achievement_{entry["name"]}_long_description\n"
                       f"}}\n\n")
        gui_file.write(f"custom_text_box = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_background\n"
                       f"}}\n\n")
        gui_file.write(f"custom_button = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_description\n"
                       f"}}\n\n")
        gui_file.write(f"custom_button = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_status\n"
                       f"}}\n\n")
        gui_file.write(f"custom_text_box = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_status\n"
                       f"}}\n")
        gui_file.write(f"custom_button = {{\n"
                       f"\tname = to_achievement_completed_{entry["name"]}_description\n"
                       f"}}\n")
        # if has_province_decision(entry):
        #     gui_file.write(f"custom_button = {{\n"
        #                    f"\tname = to_achievement_{entry["name"]}_province_decision_button_highlight\n"
        #                    f"\tpotential = {{ to_achievement_province_decision_shown = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
        #                    f"}}\n")
        gui_file.write("#########\n\n")
        ####

        gui_file.write(f"custom_icon = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_background\n"
                       f"\ttooltip = to_achievement_{entry["name"]}_long_description\n"
                       f"}}\n\n")
        # gui_file.write(f"custom_button = {{\n"
        #                f"\tname = to_achievement_{entry["name"]}_background\n"
        #                f"\ttooltip = to_achievement_{entry["name"]}_long_description\n"
        #                f"\teffect = {{\n"
        #                f"\t\tif = {{\n"
        #                f"\t\t\tlimit = {{ to_achievement_status_completed = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
        #                f"\t\t\tto_open_achievement_completed_window = yes\n"
        #                f"\t\t}}\n"
        #                f"\t}}\n"
        #                f"}}\n\n")
        gui_file.write(f"custom_text_box = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_title\n"
                       f"}}\n\n")
        gui_file.write(f"custom_text_box = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_description\n"
                       f"}}\n\n")
        gui_file.write(f"custom_icon = {{\n"
                       f"\tname = to_achievement_{entry["name"]}_status\n"
                       f"\tframe = {{\n"
                       f"\t\tnumber = 2\n"
                       f"\t\ttrigger = {{ to_achievement_status_completed = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                       f"\t}}\n"
                       f"\tframe = {{\n"
                       f"\t\tnumber = 3\n"
                       f"\t\ttrigger = {{ to_achievement_{entry["name"]}_status_failed = yes }}\n"
                       f"\t}}\n"
                       f"\tframe = {{\n"
                       f"\t\tnumber = 1\n"
                       f"\t\ttrigger = {{}}\n"
                       f"\t}}\n"
                       f"}}\n\n")
        if has_province_decision(entry):
            gui_file.write(f"custom_button = {{\n"
                           f"\tname = to_achievement_{entry["name"]}_province_decision_button\n"
                           f"\ttooltip = to_achievement_{entry["name"]}_province_decision_button_tooltip\n"
                           f"\teffect = {{ to_enable_achievement_province_decision = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                           f"}}\n")
            gui_file.write(f"custom_icon = {{\n"
                           f"\tname = to_achievement_{entry["name"]}_province_decision_button_highlight\n"
                           f"\tpotential = {{ to_achievement_province_decision_shown = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                           f"}}\n")

        gui_file.write(f"custom_window = {{\n"
                       f"\tname = to_achievement_completed_{entry["name"]}\n"
                       f"\tpotential = {{ to_achievement_completed_window_visible = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                       f"}}\n\n")
        gui_file.write(f"custom_text_box = {{\n"
                       f"\tname = to_achievement_completed_{entry["name"]}_description\n"
                       f"}}\n\n")
        gui_file.write(f"custom_button = {{\n"
                       f"\tname = to_achievement_completed_{entry["name"]}_close\n"
                       f"\teffect = {{\n"
                       f"\t\tto_close_achievement_completed_window = {{ ACHIEVEMENT = {entry["name"]} }}\n"
                       f"\t}}\n"
                       f"}}\n\n")
        if has_development_score(entry):
            gui_file.write(f"custom_text_box = {{\n"
                           f"\tname = to_achievement_completed_{entry["name"]}_score\n"
                           f"\tpotential = {{ check_variable = {{ which = to_achievement_{entry["name"]}_score value = 1 }} }}\n"
                           f"}}\n\n")

        gfx_file.write(f"\tspriteType = {{\n"
                       f"\t\tname = \"GFX_to_achievement_{entry["name"]}_icon\"\n"
                       f"\t\ttexturefile = \"gfx//interface//TO_achievements//icons//{entry["name"]}.dds\"\n"
                       f"\t}}\n\n")

        gfx_file.write(f"\tspriteType = {{\n"
                       f"\t\tname = \"GFX_to_achievement_{entry["name"]}_icon_big\"\n"
                       f"\t\ttexturefile = \"gfx//interface//TO_achievements//icons//{entry["name"]}__big.dds\"\n"
                       f"\t}}\n\n")

        loc_file.write(f" to_achievement_{entry["name"]}_title:0 \"{entry["title"]}\"\n"
                       f" to_achievement_{entry["name"]}_description:0 \"{entry["trigger_description"]}\"\n"
                       f" to_achievement_completed_{entry["name"]}_description:0 \"§g{entry["description"]}§!\"\n")
        if has_development_score(entry):
            loc_file.write(f" to_achievement_completed_{entry["name"]}_score:0 "
                           f"\"Achievement Score: §Y[Root.to_achievement_{entry["name"]}_score.GetValue]§!\\n"
                           f"(From Development: §Y[Root.to_achievement_{entry["name"]}_score_total_development.GetValue]§!, "
                           f"From Subject Development: §Y[Root.to_{entry["name"]}_score_subject_development.GetValue]§!)\"\n")
            loc_file.write(f" to_achievement_completed_{entry["name"]}_score_entry:0 "
                           f"\"Achievement Score: §Y[Root.to_achievement_{entry["name"]}_score.GetValue]§!\\n"
                           f"-From Development: §Y[Root.to_achievement_{entry["name"]}_score_total_development.GetValue]§!\\n"
                           f"-From Subject Development: §Y[Root.to_{entry["name"]}_score_subject_development.GetValue]§!\"\n")

        if "fail_conditions" in entry:
            for condition in entry["fail_conditions"]:
                if condition_only_shown_when_true(condition):
                    if f"to_achievement_FullCondition_{condition["trigger"]}_tt" not in loc_entries_added:
                        loc_entries_added.add(f"to_achievement_FullCondition_{condition["trigger"]}_tt")
                        loc_file.write(f" to_achievement_FullCondition_{condition["trigger"]}_tt:0 "
                                       f"\"[Root.ToAchievements_{condition["trigger"]}]{condition["text"]}\\n\"\n")

        loc_file.write(f" to_achievement_{entry["name"]}_long_description:0 \"")
        # loc_file.write(
        #     f"§RWe will no longer be able to complete the achievement if any of the following is true:§!\\n")
        # loc_file.write(f"[Root.ToAchievements_to_did_not_start_on_ironman]Did NOT start the game on Ironman mode.\\n")
        loc_file.write("[Root.ToAchievements_checkIronman]")
        if "fail_conditions" in entry and len(entry["fail_conditions"]) > 0:
            if has_always_visible_fail_condition(entry["fail_conditions"]):
                loc_file.write(
                    f"{fail_conditions_intro}")
            else:
                loc_file.write(
                    f"[Root.ToAchievements_FailConditionsIntroText_{entry["name"]}]")
            for condition in entry["fail_conditions"]:
                if not condition_only_shown_when_true(condition):
                    loc_file.write(f"[Root.ToAchievements_{condition["trigger"]}]{condition["text"]}\\n")
                else:
                    loc_file.write(f"[Root.ToAchievements_FullCondition_{condition["trigger"]}]")
        loc_file.write(f"\\n§GThe achievement will be completed once all of the following is true:§!\\n")
        for index, condition in enumerate(entry["success_conditions"]):
            loc_file.write(f"[Root.ToAchievements_{condition["trigger"]}]{condition["text"]}")
            # if index != len(entry["success_conditions"]) - 1:
            loc_file.write("\\n")
        loc_file.write("\\n")
        if has_development_score(entry):
            loc_file.write(f"[Root.ToAchievements_{entry["name"]}_score]")
        loc_file.write("\"\n")

        if has_province_decision(entry):
            loc_file.write(f" to_show_achievement_provinces_decision_{entry["name"]}_tt:0 \""
                           f"Enables §Y£icon_achievement£{entry["title"]} Status§! decision, which we can use to "
                           f"highlight the provinces still required to complete the achievement.\"\n")
            loc_file.write(f" to_hide_achievement_provinces_decision_{entry["name"]}_tt:0 \""
                           f"Disables §Y£icon_achievement£{entry["title"]} Status§! decision.\"\n")
            loc_file.write(f" to_achievement_provinces_decision_{entry["name"]}_title:0 \""
                           f"£icon_achievement£{entry["title"]} Status\"\n")
            loc_file.write(f" to_achievement_provinces_decision_{entry["name"]}_desc:0 \""
                           f"Province highlight shows the provinces that don't yet meet the conditions for "
                           f"§Y{entry["title"]}§! achievement.\"\n")
            loc_file.write(f" to_achievement_{entry["name"]}_province_decision_button_tooltip:0 \""
                           f"[Root.ToAchievements_show_province_decision_tooltip_{entry["name"]}]\"\n")
            cl_file.write(f"defined_text = {{\n"
                          f"    name = ToAchievements_show_province_decision_tooltip_{entry["name"]}\n"
                          f"    text = {{\n"
                          f"        trigger = {{ to_achievement_province_decision_shown = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                          f"        localisation_key = to_hide_achievement_provinces_decision_{entry["name"]}_tt\n"
                          f"    }}\n"
                          f"    text = {{\n"
                          f"        localisation_key = to_show_achievement_provinces_decision_{entry["name"]}_tt\n"
                          f"    }}\n"
                          f"}}\n\n")

        if "fail_conditions" in entry:
            if not has_always_visible_fail_condition(entry["fail_conditions"]):
                cl_file.write(f"defined_text = {{\n"
                              f"    name = ToAchievements_FailConditionsIntroText_{entry["name"]}\n"
                              f"    text = {{\n"
                              f"        trigger = {{\n"
                              f"            OR = {{\n")
                for condition in entry["fail_conditions"]:
                    if condition_only_shown_when_true(condition):
                        cl_file.write(f"                {condition["trigger"]} = yes\n")
                cl_file.write(f"            }}\n"
                              f"        }}\n"
                              f"        localisation_key = to_achievements_fail_condition_intro_tt\n"
                              f"    }}\n"
                              f"    text = {{\n"
                              f"        localisation_key = to_empty_string_tt\n"
                              f"    }}\n"
                              f"}}\n\n")
            for condition in entry["fail_conditions"]:
                if condition_only_shown_when_true(condition):
                    if f"ToAchievements_FullCondition_{condition["trigger"]}" not in cl_entries_added:
                        cl_entries_added.add(f"ToAchievements_FullCondition_{condition["trigger"]}")
                        cl_file.write(f"defined_text = {{\n"
                                      f"    name = ToAchievements_FullCondition_{condition["trigger"]}\n"
                                      f"    text = {{\n"
                                      f"        trigger = {{ {condition["trigger"]} = yes }}\n"
                                      f"        localisation_key = to_achievement_FullCondition_{condition["trigger"]}_tt\n"
                                      f"    }}\n"
                                      f"    text = {{\n"
                                      f"        localisation_key = to_empty_string_tt\n"
                                      f"    }}\n"
                                      f"}}\n\n")
                if f"ToAchievements_{condition["trigger"]}" not in cl_entries_added:
                    cl_entries_added.add(f"ToAchievements_{condition["trigger"]}")
                    cl_file.write(f"defined_text = {{\n"
                                  f"    name = ToAchievements_{condition["trigger"]}\n"
                                  f"    text = {{\n"
                                  f"        trigger = {{ {condition["trigger"]} = yes }}\n"
                                  f"        localisation_key = to_red_y_icon_tt\n"
                                  f"    }}\n"
                                  f"    text = {{\n"
                                  f"        localisation_key = to_green_x_icon_tt\n"
                                  f"    }}\n"
                                  f"}}\n\n")

        for condition in entry["success_conditions"]:
            cl_file.write(f"defined_text = {{\n"
                          f"    name = ToAchievements_{condition["trigger"]}\n"
                          f"    text = {{\n"
                          f"        trigger = {{ {condition["trigger"]} = yes }}\n"
                          f"        localisation_key = to_y_icon_tt\n"
                          f"    }}\n")
            if "partial_trigger" in condition:
                cl_file.write(f"    text = {{\n"
                              f"        trigger = {{ {condition["partial_trigger"]} = yes }}\n"
                              f"        localisation_key = to_yellow_y_icon_tt\n"
                              f"    }}\n")
            cl_file.write(f"    text = {{\n"
                          f"        localisation_key = to_x_icon_tt\n"
                          f"    }}\n"
                          f"}}\n\n")
        if has_development_score(entry):
            cl_file.write(f"defined_text = {{\n"
                          f"    name = ToAchievements_{entry["name"]}_score\n"
                          f"    text = {{\n"
                          f"        trigger = {{ check_variable = {{ which = to_achievement_{entry["name"]}_score value = 1 }} }}\n"
                          f"        localisation_key = to_achievement_completed_{entry["name"]}_score_entry\n"
                          f"    }}\n"
                          f"    text = {{\n"
                          f"        localisation_key = to_empty_string_tt\n"
                          f"    }}\n"
                          f"}}\n\n")

        if true_index % 2 == 0:
            x = left_margin
        else:
            x = left_margin + x_spacing
        y = top_margin + true_index // 2 * y_spacing

        indentation1 = "\t\t\t\t\t"
        indentation2 = "\t\t\t\t\t\t"

        interface_file.write(f"{indentation1}iconType = {{\n"
                             f"{indentation2}name = \"to_achievement_{entry["name"]}_icon\"\n"
                             f"{indentation2}position = {{ x = {x + icon_offset_x} y = {y + icon_offset_y} }}\n"
                             f"{indentation2}quadTextureSprite = \"GFX_to_achievement_{entry["name"]}_icon\"\n"
                             f"{indentation2}alwaystransparent = yes\n"
                             # f"{indentation2}scripted = yes\n"
                             f"{indentation1}}}\n\n")

        interface_file.write(f"{indentation1}iconType = {{\n"
                             f"{indentation2}name = \"to_achievement_{entry["name"]}_background\"\n"
                             f"{indentation2}position = {{ x = {x} y = {y} }}\n"
                             f"{indentation2}quadTextureSprite = \"GFX_to_achievement_entry_{entry["difficulty"]}\"\n"
                             f"{indentation2}scripted = yes\n"
                             f"{indentation1}}}\n\n")

        # interface_file.write(f"{indentation1}guiButtonType = {{\n"
        #                      f"{indentation2}name = \"to_achievement_{entry["name"]}_background\"\n"
        #                      f"{indentation2}position = {{ x = {x} y = {y} }}\n"
        #                      f"{indentation2}quadTextureSprite = \"GFX_to_achievement_entry_{entry["difficulty"]}\"\n"
        #                      f"{indentation2}scripted = yes\n"
        #                      f"{indentation1}}}\n\n")

        interface_file.write(f"{indentation1}instantTextBoxType = {{\n"
                             f"{indentation2}name = \"to_achievement_{entry["name"]}_title\"\n"
                             f"{indentation2}position = {{ x = {x + title_offset_x} y = {y + title_offset_y} }}\n"
                             f"{indentation2}font = \"{title_font}\"\n"
                             f"{indentation2}maxWidth = {title_width}\n"
                             f"{indentation2}maxHeight = 22\n"
                             f"{indentation2}fixedsize = yes\n"
                             f"{indentation2}scripted = yes\n"
                             f"{indentation2}alwaystransparent = yes\n"
                             f"{indentation1}}}\n\n")

        interface_file.write(f"{indentation1}instantTextBoxType = {{\n"
                             f"{indentation2}name = \"to_achievement_{entry["name"]}_description\"\n"
                             f"{indentation2}position = {{ x = {x + description_offset_x} y = {y + description_offset_y} }}\n"
                             f"{indentation2}font = \"{description_font}\"\n"
                             f"{indentation2}maxWidth = {entry["desc_width"] if "desc_width" in entry else description_width}\n"
                             f"{indentation2}maxHeight = 70\n"
                             f"{indentation2}fixedsize = yes\n"
                             f"{indentation2}scripted = yes\n"
                             f"{indentation2}alwaystransparent = yes\n"
                             f"{indentation1}}}\n\n")

        interface_file.write(f"{indentation1}iconType = {{\n"
                             f"{indentation2}name = \"to_achievement_{entry["name"]}_status_background\"\n"
                             f"{indentation2}position = {{ "
                             f"x = {x + status_background_offset_x + (status_background_offset_x_low_diff if has_province_decision(entry) else 0)} "
                             f"y = {y + status_background_offset_y + (status_background_offset_y_low_diff if has_province_decision(entry) else 0)} "
                             f"}}\n"
                             f"{indentation2}quadTextureSprite = \"GFX_to_achievement_status_background\"\n"
                             f"{indentation2}alwaystransparent = yes\n"
                             f"{indentation1}}}\n\n")

        interface_file.write(f"{indentation1}iconType = {{\n"
                             f"{indentation2}name = \"to_achievement_{entry["name"]}_status\"\n"
                             f"{indentation2}position = {{ "
                             f"x = {x + status_offset_x + (status_offset_x_low_diff if has_province_decision(entry) else 0)} "
                             f"y = {y + status_offset_y + (status_offset_y_low_diff if has_province_decision(entry) else 0)} "
                             f"}}\n"
                             f"{indentation2}quadTextureSprite = \"GFX_to_achievement_status_icons\"\n"
                             f"{indentation2}scripted = yes\n"
                             f"{indentation2}alwaystransparent = yes\n"
                             f"{indentation1}}}\n\n")

        if has_province_decision(entry):
            province_decision_button_x = x + province_decision_offset_x
            province_decision_button_y = y + province_decision_offset_y
            interface_file.write(f"{indentation1}guiButtonType = {{\n"
                                 f"{indentation2}name = \"to_achievement_{entry["name"]}_province_decision_button\"\n"
                                 f"{indentation2}position = {{ x = {province_decision_button_x} y = {province_decision_button_y} }}\n"
                                 f"{indentation2}quadTextureSprite = \"GFX_to_province_decision_button\"\n"
                                 f"{indentation2}scripted = yes\n"
                                 f"{indentation1}}}\n\n")

            interface_file.write(f"{indentation1}iconType = {{\n"
                                 f"{indentation2}name = \"to_achievement_{entry["name"]}_province_decision_button_highlight\"\n"
                                 f"{indentation2}position = {{ x = {province_decision_button_x} y = {province_decision_button_y} }}\n"
                                 f"{indentation2}quadTextureSprite = \"GFX_to_province_decision_button_highlight\"\n"
                                 f"{indentation2}alwaystransparent = yes\n"
                                 f"{indentation2}scripted = yes\n"
                                 f"{indentation1}}}\n\n")

        indentation0 = "\t\t"
        indentation1 = "\t\t\t"
        indentation2 = "\t\t\t\t"

        completion_file.write(f"{indentation0}windowType = {{\n"
                              f"{indentation1}name = \"to_achievement_completed_{entry["name"]}\"\n"
                              f"{indentation1}position = {{ x = -265 y = -225 }}\n"
                              f"{indentation1}Orientation = \"CENTER\"\n"
                              f"{indentation1}scripted = yes\n\n")

        completion_file.write(f"{indentation1}iconType = {{\n"
                              f"{indentation2}name = \"to_achievement_completed_{entry["name"]}_background\"\n"
                              f"{indentation2}position = {{ x = 0 y = 0 }}\n"
                              f"{indentation2}quadTextureSprite = \"GFX_to_achievement_completed_window_{entry["difficulty"]}\"\n"
                              f"{indentation1}}}\n\n")

        completed_icon_offset = {"x": completed_icon_offset_x, "y": completed_icon_offset_y}
        if "frame_size" in entry:
            completed_icon_offset["x"] += int((224 - entry["frame_size"][0]) / 2)
            completed_icon_offset["y"] += int((133 - entry["frame_size"][1]) / 2)

        completion_file.write(f"{indentation1}iconType = {{\n"
                              f"{indentation2}name = \"to_achievement_{entry["name"]}_icon_big\"\n"
                              f"{indentation2}position = {{ x = {completed_icon_offset["x"]} y = {completed_icon_offset["y"]} }}\n"
                              f"{indentation2}quadTextureSprite = \"GFX_to_achievement_{entry["name"]}_icon_big\"\n"
                              f"{indentation1}}}\n\n")

        frame_texture = "GFX_achievement_complete_image_frame"
        if "frame_size" in entry:
            frame_texture = f"GFX_achievement_complete_image_frame_{entry["frame_size"][0]}x{entry["frame_size"][1]}"

        completion_file.write(f"{indentation1}iconType = {{\n"
                              f"{indentation2}name = \"to_achievement_completed_image_frame\"\n"
                              f"{indentation2}position = {{ x = 0 y = 0 }}\n"
                              f"{indentation2}quadTextureSprite = \"{frame_texture}\"\n"
                              f"{indentation1}}}\n\n")

        completion_file.write(f"{indentation1}instantTextBoxType = {{\n"
                              f"{indentation2}name = \"to_achievement_completed\"\n"
                              f"{indentation2}position = {{ x = {completed_title_text_offset_x} y = {completed_title_text_offset_y} }}\n"
                              f"{indentation2}font = \"{completed_title_text_font}\"\n"
                              f"{indentation2}maxWidth = {completed_title_text_width}\n"
                              f"{indentation2}maxHeight = 22\n"
                              f"{indentation2}fixedsize = yes\n"
                              f"{indentation2}format = center\n"
                              f"{indentation2}scripted = yes\n"
                              f"{indentation1}}}\n\n")

        completion_file.write(f"{indentation1}instantTextBoxType = {{\n"
                              f"{indentation2}name = \"to_achievement_{entry["name"]}_title\"\n"
                              f"{indentation2}position = {{ x = {completed_title_offset_x} y = {completed_title_offset_y} }}\n"
                              f"{indentation2}font = \"{completed_title_font}\"\n"
                              f"{indentation2}maxWidth = {completed_title_width}\n"
                              f"{indentation2}maxHeight = 22\n"
                              f"{indentation2}fixedsize = yes\n"
                              f"{indentation2}format = center\n"
                              f"{indentation2}scripted = yes\n"
                              f"{indentation1}}}\n\n")

        completion_file.write(f"{indentation1}instantTextBoxType = {{\n"
                              f"{indentation2}name = \"to_achievement_completed_{entry["name"]}_description\"\n"
                              f"{indentation2}position = {{ x = {completed_description_offset_x} y = {completed_description_offset_y} }}\n"
                              f"{indentation2}font = \"{completed_description_font}\"\n"
                              f"{indentation2}maxWidth = {completed_description_width}\n"
                              f"{indentation2}maxHeight = {completed_description_height}\n"
                              f"{indentation2}scrollbartype = \"standardtext_slider\"\n"
                              f"{indentation2}scripted = yes\n"
                              f"{indentation1}}}\n\n")

        if has_development_score(entry):
            completion_file.write(f"{indentation1}instantTextBoxType = {{\n"
                                  f"{indentation2}name = \"to_achievement_completed_{entry["name"]}_score\"\n"
                                  f"{indentation2}position = {{ x = {completed_score_offset_x} y = {completed_score_offset_y} }}\n"
                                  f"{indentation2}font = \"{completed_score_font}\"\n"
                                  f"{indentation2}maxWidth = {completed_score_width}\n"
                                  f"{indentation2}maxHeight = 80\n"
                                  f"{indentation2}fixedsize = yes\n"
                                  f"{indentation2}format = center\n"
                                  f"{indentation2}scripted = yes\n"
                                  f"{indentation1}}}\n\n")

        completion_file.write(f"{indentation1}guiButtonType = {{\n"
                              f"{indentation2}name = \"to_achievement_completed_{entry["name"]}_close\"\n"
                              f"{indentation2}position = {{ x = {completed_close_offset_x} y = {completed_close_offset_y} }}\n"
                              f"{indentation2}quadTextureSprite = \"button_type_9\"\n"
                              f"{indentation2}scripted = yes\n"
                              f"{indentation1}}}\n\n")

        completion_file.write(f"{indentation1}instantTextBoxType = {{\n"
                              f"{indentation2}name = \"to_achievement_completed_close_text\"\n"
                              f"{indentation2}position = {{ x = {completed_close_text_offset_x} y = {completed_close_text_offset_y} }}\n"
                              f"{indentation2}font = \"{completed_close_text_font}\"\n"
                              f"{indentation2}maxWidth = {completed_close_text_width}\n"
                              f"{indentation2}maxHeight = 22\n"
                              f"{indentation2}fixedsize = yes\n"
                              f"{indentation2}format = center\n"
                              f"{indentation2}alwaystransparent = yes\n"
                              f"{indentation2}scripted = yes\n"
                              f"{indentation1}}}\n\n")

        completion_file.write(f"{indentation0}}}\n\n")

        if "generate_event" in entry and entry["generate_event"] is True:
            events_file.write(f"country_event = {{\n"
                              f"\tid = {events_namespace}.{events_starting_id}\n"
                              f"\ttitle = nhs2_hidden.t\n"
                              f"\tdesc = nhs2_hidden.d\n"
                              f"\tpicture = ADVISOR_eventPicture\n"
                              f"\n"
                              f"\thidden = yes\n"
                              f"\n"
                              f"\ttrigger = {{\n"
                              f"\t\tto_has_elysian_achievements = yes\n"
                              f"\t\tNOT = {{ to_achievement_status_completed = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                              f"\t\tNOT = {{ to_achievement_{entry["name"]}_status_failed = yes }}\n"
                              f"\t\tto_achievement_{entry["name"]}_can_be_completed = yes\n"
                              f"\t}}\n"
                              f"\n"
                              f"\timmediate = {{\n"
                              f"\t\tto_complete_achievement = {{\n"
                              f"\t\t\tACHIEVEMENT = {entry["name"]}\n")
            if has_development_score(entry):
                events_file.write(f"\t\t\tADDITIONAL_EFFECT = \"to_compute_achievement_score_from_development = {{ ACHIEVEMENT = {entry["name"]} }}\"\n")
            events_file.write(f"\t\t}}\n"
                              f"\t}}\n"
                              f"\n"
                              f"\toption = {{\n"
                              f"\t\tname = nhs2_hidden.a\n"
                              f"\t}}\n"
                              f"}}\n\n")
            events_starting_id += 1

        scripted_triggers_file.write(f"to_achievement_{entry["name"]}_can_be_completed = {{\n")
        for condition in entry["success_conditions"]:
            scripted_triggers_file.write(f"\t{condition["trigger"]} = yes\n")
        scripted_triggers_file.write("}\n\n")

        if "generate_check" in entry and entry["generate_check"] is True:
            scripted_effects_file.write(f"to_achievement_{entry["name"]}_check = {{\n"
                                        f"\thidden_effect = {{\n"
                                        f"\t\tif = {{\n"
                                        f"\t\t\tlimit = {{\n"
                                        f"\t\t\t\tNOT = {{ to_achievement_status_completed = {{ ACHIEVEMENT = {entry["name"]} }} }}\n"
                                        f"\t\t\t\tNOT = {{ to_achievement_{entry["name"]}_status_failed = yes }}\n"
                                        f"\t\t\t\tto_achievement_{entry["name"]}_can_be_completed = yes\n"
                                        f"\t\t\t}}\n"
                                        f"\t\t\tto_complete_achievement = {{ ACHIEVEMENT = {entry["name"]} }}\n"
                                        f"\t\t}}\n"
                                        f"\t}}\n"
                                        f"}}\n\n")

    # interface_file.write("\t\t\t}\n")
    # interface_file.write("\t\t}\n")
    gfx_file.write("}")

gui_file.close()
loc_file.close()
interface_file.close()
completion_file.close()
gfx_file.close()
cl_file.close()
events_file.close()
scripted_triggers_file.close()
