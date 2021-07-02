definition_file = "definition_pdx.csv"
output_file = "output.txt"
buffer_size = 419
start_id = 4942


def get_existing_colors():
    colors = []
    definition = open(definition_file)
    for line in definition:
        content = line.strip().split(";")
        colors.append(content[1] + ";" + content[2] + ";" + content[3])
    definition.close()
    return colors


def write_buffer(colors):
    output = open(output_file, "w")
    counter = 0
    for r in range(256):
        for g in range(256):
            for b in range(256):
                if counter == buffer_size:
                    output.close()
                    return
                color = str(r) + ";" + str(g) + ";" + str(b)
                if color in colors:
                    # print(color)
                    continue
                print(start_id + counter, end=" ")
                output.write(str(start_id + counter) + ";" + color + ";" + "UNUSED" + str(counter + 1) + ";x\n")
                counter += 1

    output.close()
    return


colors = get_existing_colors()
write_buffer(colors)
