from jinja2 import Template
import os

output_file = "o_ruler_with_stats.txt"


template = Template('''{% for i in range(6, -1 , -1) %}
    {%- if loop.first -%}
    if = {
    {%- else -%}
    else_if = {
    {%- endif -%}
        limit = { check_variable = { which = $ADM_VARIABLE$ value = {{ i }} } }
        {% for j in range(6, -1 , -1) %}
        {%- if loop.first -%}
        if = {
        {%- else -%}
        else_if = {
        {%- endif -%}
            limit = { check_variable = { which = $DIP_VARIABLE$ value = {{ j }} } }
            {% for k in range(6, -1 , -1) %}
            {%- if loop.first -%}
            if = {
            {%- else -%}
            else_if = {
            {%- endif -%}
                limit = { check_variable = { which = $MIL_VARIABLE$ value = {{ k }} } } $EFFECT$ }
            {% endfor %}
        }
        {% endfor %}
    }{{" "}}
    {% endfor %}
''')

f = open(output_file, "w")
f.write("to_generate_ruler_from_variable = {\n")
f.write(f"# Code generated by {os.path.basename(os.getcwd())}/{os.path.basename(__file__)}\n")
f.write("\t")
for i in range(6, -1, -1):
    if i == 6:
        f.write("if = { ")
    else:
        f.write("else_if = { ")
    f.write("limit = { check_variable = { which = $ADM_VARIABLE$ value = %d } } " % i)
    for j in range(6, -1, -1):
        if j == 6:
            f.write("if = { ")
        else:
            f.write("else_if = { ")
        f.write("limit = { check_variable = { which = $DIP_VARIABLE$ value = %d } } " % j)
        for k in range(6, -1, -1):
            if k == 6:
                f.write("if = { ")
            else:
                f.write("else_if = { ")
            f.write("limit = { check_variable = { which = $MIL_VARIABLE$ value = %d } } " % k)
            f.write("$EFFECT$ = { ADM = %d DIP = %d MIL = %d } " % (i, j, k))
            f.write("} ")
        f.write("} ")
    f.write("} ")
f.write("\n}")
f.close()

