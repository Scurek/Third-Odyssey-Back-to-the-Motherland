import re

input_file = "../../../deploy/common/province_names/greek.txt"
city_names_file = "city_names.txt"
output_file = "output.txt"

city_names = {}

with open(city_names_file) as file:
    lines = file.readlines()
    for line in lines:
        mod_line = re.sub(r'([={}]|rename_capital)', '', line)
        # mod_line = re.sub(' +', ' ', mod_line)

        comp = mod_line.split("\"")
        city_names[comp[0].strip()] = comp[1]

print(city_names)
with open(input_file) as file:
    with open(output_file, 'w') as o:
        lines = file.readlines()
        for line in lines:
            mod_line = re.sub(r'[={}\n\t]', '', line)
            comp = mod_line.split("\"")
            comp[0] = comp[0].strip()
            if comp[0] not in city_names or len(comp) > 3:
                if line[0] == "#" or "#" not in line:
                    o.write(line)
                    continue
                comp2 = line.split("#")
                name_string = comp2[0].strip()
                o.write("%s%s# %s\n" % (name_string,
                                        str.join("", (" " for _ in range(40 - len(name_string)))),
                                        comp2[1].strip()))
                continue
            name_string = "%s = { \"%s\" \"%s\" }" % (comp[0], comp[1], city_names[comp[0]])
            o.write("%s%s%s\n" % (name_string,
                                  str.join("", (" " for _ in range(40 - len(name_string)))),
                                  comp[2].strip()))
