from jinja2 import Template, Environment
from exarch_tags import tags

output_file = "exarch_extra_merchant_output.txt"

template = Template('''OR = {
{%- for tag in tags %}
    AND = {
        tag = {{ tag }}
        NOT = {
            any_province = {
                nhs_{{ tag }}_province = yes
                NOT = { owned_by = {{ tag }} }
            }
        }
    }
{%- endfor %}
}
''')

f = open(output_file, "w")
f.write(template.render(tags=tags))
f.close()