from jinja2 import Template, Environment

output_file = "output.txt"

START = 50
STEP = 5

# sequence = range(5000, 0, -STEP)

sequence = [i for i in range(START, 0, -STEP)]
sequence.append(1)
sequence.append(0)

template = Template('''{%- for pop in sequence %}
{%- if loop.first -%}
if = {
{%- else %}
else_if = {
{%- endif %}
    limit = {
        {%- if loop.first %}
        native_size = {{ pop }}
        {%- elif loop.last %}
        NOT = { native_size = {{ loop.previtem }} }
        {%- else %}
        NOT = { native_size = {{ loop.previtem }} }
        native_size = {{ pop }}
        {%- endif %}
        NOT = { has_province_flag = to_local_natives_num_{{ pop }} }
    }
{%- for pop_flag in sequence %}
    {%- if pop_flag == pop %}
    set_province_flag = to_local_natives_num_{{ pop_flag }}
    {%- else %}
    clr_province_flag = to_local_natives_num_{{ pop_flag }}
    {%- endif %}
{%- endfor %}
}
{%- endfor %}
''')

f = open(output_file, "w")
f.write(template.render(sequence=sequence))
f.close()
