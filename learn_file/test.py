import json


def read_file(file_path):
    with open(file_path, 'r') as fs:
        temp = json.load(fs)
        print(temp)
        target = temp["key1"]
        print(target)


read_file('demojsonfile.json')