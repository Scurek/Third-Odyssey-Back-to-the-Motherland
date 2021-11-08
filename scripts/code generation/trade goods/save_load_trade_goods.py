from jinja2 import Template, Environment

output_save = "output_save.txt"
output_load = "output_load.txt"

trade_goods = [
    "grain",
    "wine",
    "wool",
    "cloth",
    "fish",
    "fur",
    "salt",
    "naval_supplies",
    "copper",
    "gold",
    "iron",
    "slaves",
    "ivory",
    "tea",
    "chinaware",
    "spices",
    "coffee",
    "cotton",
    "sugar",
    "tobacco",
    "cocoa",
    "silk",
    "elysian_silk",
    "skoros_silk",
    "tropical_wood",
    "dyes",
    "norse_mead",
    "livestock",
    "incense",
    "glass",
    "gems",
    "paper",
    "coal",
    "cloves",
    "unknown",
    "coal_2",
    "nothing"
]

clr_flags = Template('''{%- for trade_good in trade_goods %}
    clr_province_flag = nhs_had_{{ trade_good }}_tg
{%- endfor %}
''')

save = Template('''{%- for trade_good in trade_goods %}
{%- if loop.first -%}
    if = {
{%- else %}
    else_if = {
{%- endif %} limit = { trade_goods = {{ trade_good }} } set_province_flag = nhs_had_{{ trade_good }}_tg }
{%- endfor %}
''')

load = Template('''{%- for trade_good in trade_goods %}
{%- if loop.first -%}
    if = {
{%- else %}
    else_if = {
{%- endif %} limit = { has_province_flag = nhs_had_{{ trade_good }}_tg } change_trade_goods = {{ trade_good }} }
{%- endfor %}
''')

f = open(output_save, "w")
f.write(clr_flags.render(trade_goods=trade_goods))
f.write("\n")
f.write(save.render(trade_goods=trade_goods))
f.close()

f = open(output_load, "w")
f.write(load.render(trade_goods=trade_goods))
f.write(clr_flags.render(trade_goods=trade_goods))
f.close()
