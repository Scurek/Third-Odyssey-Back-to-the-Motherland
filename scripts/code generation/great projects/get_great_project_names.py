import json


def parse_great_project_names(file_path: str) -> [str]:
    project_names = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            if len(line) > 0 and line[0].isalpha():
                project_name = line.strip().split("=")[0].strip()
                project_names.append(project_name)

    return project_names


if __name__ == "__main__":
    great_project_file_paths = {
        "../../../deploy/common/great_projects/01_monuments.txt",
        "../../../deploy/common/great_projects/00_great_projects.txt",
        "../../../deploy/common/great_projects/TO_great_projects.txt"
    }
    project_names = []
    for file_path in great_project_file_paths:
        project_names.extend(parse_great_project_names(file_path))
    with open("monuments.json", "w") as o:
        json.dump(project_names, o, indent=2)
