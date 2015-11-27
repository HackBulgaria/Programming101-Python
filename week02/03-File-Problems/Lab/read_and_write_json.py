import json


def read_json():
    with open('colors.json', 'r') as f:
        data = json.load(f)

    return data


def write_json():
    data = read_json()

    dic = {"yellow": 125}
    data.update(dic)

    with open('colors.json', 'w') as f:
        json.dump(data, f)

