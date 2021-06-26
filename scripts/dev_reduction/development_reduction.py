output_file = "output.txt"
variable_name = "nhs_borealian_$DEVELOPMENT_TYPE$_lost"
output = ""

max_dev = 15

def tab(n):
    return n * '\t'


for i in range(max_dev, 0, -1):
    if i == max_dev:
        output += "if = {" + "\n"
    else:
        output += "else_if = {" + "\n"
    output += tab(1) + "limit = {" + "\n"
    output += tab(2) + "check_variable = {" + "\n"
    output += tab(3) + "which = " + variable_name + "\n"
    output += tab(3) + "value = " + str(i) + "\n"
    output += tab(2) + "}" + "\n"
    output += tab(1) + "}" + "\n"
    output += tab(1) + "add_$DEVELOPMENT_TYPE$ = $SIGN$" + str(i) + "\n"
    output += "}" + "\n"

f = open(output_file, "w")
f.write(output)
f.close()
