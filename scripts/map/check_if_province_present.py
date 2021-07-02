from PIL import Image

definition_file = "definition_full.csv"
province_file = "provinces.bmp"

def get_colors_from_provinces():
    im = Image.open(province_file)
    colors = []
    for color in im.getcolors(maxcolors=256 * 256 * 256):
        colors.append(color[1])
    im.close()
    return colors


def get_colors_from_definiton():
    colors = []
    definition = open(definition_file)
    for line in definition:
        content = line.strip().split(";")
        if content[4] == "RNW" or content[4].lower().startswith("unused") or content[0] == "province":
            continue
        colors.append(((int(content[1]), int(content[2]), int(content[3])), content[0]))
    definition.close()
    return colors


prov_colors = get_colors_from_provinces()
def_colors = get_colors_from_definiton()
print("Missing IDs:")
for color in def_colors:
    if color[0] not in prov_colors:
        print("ID:", color[1])
