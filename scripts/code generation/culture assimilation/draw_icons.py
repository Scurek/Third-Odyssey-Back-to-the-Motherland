from PIL import Image, ImageColor, ImageDraw

def interpolate(color1, color2, a):
    return int(color1[0] * (1 - a) + color2[0] * a), \
           int(color1[1] * (1 - a) + color2[1] * a), int(color1[2] * (1 - a) +
                                                         color2[2] * a)


def btree(lst, form, body):
    if not len(lst):
        return ''
    elif len(lst) == 1:
        return body % (lst[0], lst[0])
    else:
        return form % (lst[int(len(lst) / 2)],
                       btree(lst[int(len(lst) / 2):], form, body),
                       btree(lst[:int(len(lst) / 2)], form, body))


modifiers = [{'name': 'to_culture_assimilation',
              'title': 'Cultural Assimilation',
              'desc': '[Root.GetCultureAssimilationDesc]'},
             {'name': 'to_tribal_integration',
              'title': 'Tribal Integration',
              'desc': '[Root.GetTribalIntegrationDesc]'},
             {'name': 'to_culture_assimilation_roman',
              'title': 'Symmachoi Assimilation',
              'desc': '[Root.GetSymmachoiAssimilationDesc]'},
             {'name': 'to_culture_assimilation_norse',
              'title': 'Skraeling Assimilation',
              'desc': '[Root.GetSkraelingAssimilationDesc]'}
             ]

images = [Image.open(f'{modifier["name"]}.dds') for modifier in modifiers]

# image = Image.open('to_culture_assimilation.dds')
# imageTI = Image.open('to_tribal_integration.dds')
width, height = images[0].size
# image = image.convert('RGBA')

draws = [ImageDraw.Draw(image) for image in images]
# draw = ImageDraw.Draw(image)
# drawTI = ImageDraw.Draw(imageTI)

yellow = ImageColor.getrgb('#ffbb00')
green = ImageColor.getrgb('#008000')

part_size = int(100 / width)

for index, image in enumerate(images):
    image.save(f'icons/{modifiers[index]["name"]}_0.dds')

# imageTI.save(f'icons/to_tribal_integration_0.dds')
fractions = [0]

for i in range(0, width - 4):
    shape = ((2, int(height * 0.875)), (2 + i, height))
    color = interpolate(yellow, green, i / width)
    fraction = int((i + 1) / (width - 3) * 100)
    fractions.append(fraction)
    for index, image in enumerate(images):
        draws[index].rectangle(shape, fill=color)
        image.save(f'icons/{modifiers[index]["name"]}_{fraction}.dds')

cond = 'check_variable={which=to_assimilation_progress value=%s}'
body = 'if = {limit={NOT={has_province_modifier=$MODIFIER_BASE_NAME$_%s}} ' \
       'to_remove_assimilation_modifiers=yes add_province_modifier={' \
       'name=$MODIFIER_BASE_NAME$_%s duration=-1} }'
form = 'if={limit={%s}%s}else={%s}' % (cond, '%s', '%s')

with open('to_remove_assimilation_modifiers.txt', 'w') as f:
    f.write('to_remove_assimilation_modifiers = {\n')
    for index, image in enumerate(images):
        for i in fractions:
            f.write(f'\tremove_province_modifier = {modifiers[index]["name"]}_{i}\n')
    f.write('}')

with open('to_set_correct_assimilation_modifier.txt', 'w') as f:
    f.write('to_set_correct_assimilation_modifier = { \n' + btree([i for i in fractions], form,
                                                                  body) + '}')

with open('localisation.txt', 'w') as f:
    for index, image in enumerate(images):
        for i in fractions:
            f.write(f' {modifiers[index]["name"]}_{i}:0 \"{modifiers[index]["title"]}\"\n')
            f.write(f' desc_{modifiers[index]["name"]}_{i}:0 \"{modifiers[index]["desc"]}\"\n')
    # for i in fractions:
    #     f.write(f' to_tribal_integration_{i}:0 \"Tribal Integration\"\n')
    #     f.write(f' desc_to_tribal_integration_{i}:0 \"[Root.GetTribalIntegrationDesc]\"\n')

with open('modifiers.txt', 'w') as f:
    for index, image in enumerate(images):
        for i in fractions:
            f.write(f'{modifiers[index]["name"]}_{i} = {{\n')
            f.write(f'\tpicture = \"{modifiers[index]["name"]}_{i}\"\n')
            f.write('}\n\n')
    # for i in fractions:
    #     f.write(f'to_tribal_integration_{i} = {{\n')
    #     f.write(f'\tpicture = \"to_tribal_integration_{i}\"\n')
    #     f.write('}\n\n')
