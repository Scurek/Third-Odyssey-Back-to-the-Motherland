import os

output_progress_bar = "o_progress_bar.txt"

full_frame = '''
    frame = {
        number = {i}
        trigger = {
            check_variable = {
                which = to_assimilation_progress_display
                value = {i}
            }
        }
    }'''

final_frame = '''
    frame = {
        number = 0
        trigger = { }
    }'''

with open(output_progress_bar, "w") as f:
    for i in range(100, -1, -1):
        if i != 0:
            f.write(full_frame.replace("{i}", str(i)))
        else:
            f.write(final_frame)

