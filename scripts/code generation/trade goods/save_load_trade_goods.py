from jinja2 import Template, Environment
from trade_goods import trade_goods

output_save = "output_save.txt"
output_load = "output_load.txt"


clr_flags = Template('''{%- for trade_good in trade_goods %}
    clr_province_flag = nhs_had_{{ trade_good["name"] }}_tg
{%- endfor %}
''')

save = Template('''{%- for trade_good in trade_goods %}
{%- if loop.first -%}
    if = {
{%- else %}
    else_if = {
{%- endif %} limit = { trade_goods = {{ trade_good["name"] }} } set_province_flag = nhs_had_{{ trade_good["name"] }}_tg }
{%- endfor %}
''')

load = Template('''{%- for trade_good in trade_goods %}
{%- if loop.first -%}
    if = {
{%- else %}
    else_if = {
{%- endif %} limit = { has_province_flag = nhs_had_{{ trade_good["name"] }}_tg } change_trade_goods = {{ trade_good["name"] }} }
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
