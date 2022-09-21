from jinja2 import Template
from exarchs import exarchs

output_file = "o_exarch_extra_merchant_output.txt"

template = Template('''OR = {
{%- for exarch in exarchs %}
    AND = {
        tag = {{ exarch['tag'] }}
        NOT = {
            any_province = {
                nhs_{{ exarch['tag'] }}_province = yes
                NOT = { owned_by = {{ exarch['tag'] }} }
            }
        }
    }
{%- endfor %}
}
''')

f = open(output_file, "w")
f.write(template.render(exarchs=exarchs))
f.close()