import yaml


def analyze_file(filename, key):
    with open("./data/" + filename + ".yaml", "r", encoding="utf-8") as f:
        data_list = []
        data = yaml.full_load(f)[key]
        for value in data.values():
            data_list.append(value)
        return data_list
