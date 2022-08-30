from trade_goods import trade_goods
from PIL import Image, ImageOps
import os

if not os.path.isdir("icons"):
    os.makedirs("icons")

DESIRED_SIZE = [22, 22]

circle_icon = Image.open('base/circle.png')
circle_selected_icon = Image.open('base/circle_selected.png')
icons_small = Image.open('base/resources_small.dds')
icons_font = Image.open('base/resources_font.dds')
icons_font_small = Image.open('base/resources_font_small.dds')

for index, trade_good in enumerate(trade_goods):
    if "no_icon" in trade_good:
        continue
    icons = icons_font
    if trade_good["fontsize"] == "small":
        icons = icons_font_small
    font_size = icons.size[1]
    icon = icons.crop((index * font_size, 0, index * font_size + font_size, font_size))
    if DESIRED_SIZE[0] > icon.size[0] or DESIRED_SIZE[1] > icon.size[1]:
        left = int((DESIRED_SIZE[0] - icon.size[0]) / 2)
        top = int((DESIRED_SIZE[1] - icon.size[1]) / 2) + trade_good["offset"]
        right = DESIRED_SIZE[0] - icon.size[0] - left
        bottom = DESIRED_SIZE[1] - icon.size[1] - top
        icon = ImageOps.expand(icon, border=(left, top, right, bottom), fill=(0, 0, 0, 0))
    elif "offset" in trade_good:
        top = 0
        bottom = 0
        if trade_good["offset"] > 0:
            top = trade_good["offset"]
        else:
            bottom = -trade_good["offset"]
        icon = ImageOps.expand(icon, border=(0, top, 0, bottom), fill=(0, 0, 0, 0))
        icon = icon.crop((0, 0 + bottom, icon.size[0], icon.size[1] - top))
    print(icon.size)
    icon.save(f'icons/icon_tg_{trade_good["name"]}.dds')

    if "no_circle_icon" in trade_good:
        continue
    icons = icons_small
    font_size = icons.size[1]
    icon = icons.crop((index * font_size, 0, index * font_size + font_size, font_size))
    if "circle_resize" in trade_good:
        icon = icon.resize((trade_good["circle_resize"], trade_good["circle_resize"]), Image.BICUBIC)
    selected_icon = circle_selected_icon.copy()
    unselected_icon = circle_icon.copy()
    left = int((selected_icon.size[0] - icon.size[0]) / 2)
    top = int((selected_icon.size[1] - icon.size[1]) / 2)
    selected_icon.alpha_composite(icon, (left, top))
    unselected_icon.alpha_composite(icon, (left, top))
    selected_icon.save(f'icons/circle_{trade_good["name"]}_selected.dds')
    unselected_icon.save(f'icons/circle_{trade_good["name"]}.dds')
