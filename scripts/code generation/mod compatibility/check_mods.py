import os

EU4_WORKSHOP_DIRECTORY = "F:\\SteamLibrary\\steamapps\\workshop\\content\\236850"

IGNORED_DIRECTORIES = [".idea", ".git", ".archive", "map\\terrain"]
ADDED_FOLDERS = ["common\\diplomatic_actions", "common\\static_modifiers"]
IGNORED_FILES = ["interface\\frontend.gui", "gfx\\FX\\pdxmap.shader", ".\\descriptor.mod", ".\\README.md", ".\\.gitignore", ".\\thumbnail.png"]


def create_file_list(path):
    file_set = set()
    for root, dirs, files in os.walk(path):
        relative_path = os.path.relpath(root, path)
        if relative_path in IGNORED_DIRECTORIES:
            continue
        if relative_path in ADDED_FOLDERS:
            file_set.add(relative_path)
        for file in files:
            file_path = os.path.join(relative_path, file)
            if file_path in IGNORED_FILES:
                continue
            file_set.add(file_path)
    return file_set


def get_mod_name(path):
    with open(os.path.join(path, "descriptor.mod")) as descriptor:
        for line in descriptor:
            if line.startswith("name="):
                return line[6:-2]


mod_file_set = create_file_list(os.path.join(EU4_WORKSHOP_DIRECTORY,
                              "C:\\Users\\Uros\\Documents\\Paradox Interactive\\Europa Universalis IV\\mod\\Third-Odyssey-Development\\deploy"))

with open("compatible_mods.txt", "w") as f:
    for name in os.listdir(EU4_WORKSHOP_DIRECTORY):
        mod_path = os.path.join(EU4_WORKSHOP_DIRECTORY, name)
        if not os.path.isfile(os.path.join(mod_path, "descriptor.mod")):
            f.write(os.path.basename(mod_path) + "-- No descriptor found\n\n")
            continue

        mod_name = get_mod_name(mod_path)

        file_set = create_file_list(mod_path)
        duplicate_files = mod_file_set & file_set
        f.write("-> " + mod_name + "\n")
        f.write("Mod Id: " + name + "\n")
        if len(duplicate_files) > 0:
            f.write("Duplicate files:\n")
            for entry in duplicate_files:
                f.write(entry + "\n")
        f.write("\n")



