import os

YEARS = 20
output_file_loc = "o_localisation.txt"
output_file_cl = "o_customizable_loc.txt"

file_cl = open(output_file_cl, "w")
file_loc = open(output_file_loc, "w")

bt = "\t"
file_cl.write(f"{bt}# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
file_loc.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")

for month in range(1, 13):
    passed_days = (YEARS - 1) * 365 + round((12 - month) * 30.42)

    file_cl.write(f"{bt}text = {{\n"
                  f"{bt}\tlocalisation_key = to_{month}_months_tt\n"
                  f"{bt}\ttrigger = {{\n"
                  f"{bt}\t\tFROM = {{ had_country_flag = {{ flag = to_send_trade_expedition days = {passed_days} }} }}\n"
                  f"{bt}\t}}\n"
                  f"{bt}}}\n")

    if month == 1:
        file_loc.write(f" to_{month}_months_tt:0 \"{month} Month\"\n")
    else:
        file_loc.write(f" to_{month}_months_tt:0 \"{month} Months\"\n")

for year in range(2, YEARS + 1):
    passed_days = (YEARS - year) * 365

    file_cl.write(f"{bt}text = {{\n"
                  f"{bt}\tlocalisation_key = to_{year}_years_tt\n"
                  f"{bt}\ttrigger = {{\n")
    if year != YEARS:
        file_cl.write(f"{bt}\t\t"
                      f"FROM = {{ had_country_flag = {{ flag = to_send_trade_expedition days = {passed_days} }} }}\n")
    file_cl.write(f"{bt}\t}}\n"
                  f"{bt}}}\n")

    if year == 1:
        file_loc.write(f" to_{year}_years_tt:0 \"{year} Year\"\n")
    else:
        file_loc.write(f" to_{year}_years_tt:0 \"{year} Years\"\n")

file_cl.close()
file_loc.close()