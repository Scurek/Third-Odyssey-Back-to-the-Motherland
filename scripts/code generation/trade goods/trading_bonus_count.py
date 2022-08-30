from jinja2 import Template
from trade_goods import trade_goods

output = "trading_bonus_count.txt"

AMOUNT = 20

template = Template('''if = {
    limit = {
        has_dlc = "Rule Britannia"
    }
    calc_true_if = {
        amount = {{ AMOUNT }}
        {% for trade_good in trade_goods %}
        {% if "no_bonus" not in trade_good and trade_good["name"] != "coal_2" -%}
            trading_bonus = { trade_goods = {{ trade_good["name"] }} value = yes }
        {%- endif %}
        {%- endfor %}
    }
}
else = {
    calc_true_if = {
        amount = {{ AMOUNT }}
        {% for trade_good in trade_goods %}
        {% if "no_bonus" not in trade_good and trade_good["name"] != "coal" -%}
            trading_bonus = { trade_goods = {{ trade_good["name"] }} value = yes }
        {%- endif -%}
        {%- endfor %}
    }
}
''')

f = open(output, "w")
f.write(template.render(trade_goods=trade_goods, AMOUNT=AMOUNT))
f.close()