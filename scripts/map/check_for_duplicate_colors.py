definition_file = "definition_full.csv"

def check_for_duplicates():
    colors = []
    definition = open(definition_file)
    definition.readline()
    for line in definition:
        definition.readline()
        content = line.strip().split(";")
        color = (int(content[1]), int(content[2]), int(content[3]))
        if color in colors:
            print(line)
        colors.append((color, content[0]))
    definition.close()

check_for_duplicates()
