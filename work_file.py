import json


def read_full_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readline()


def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def write_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)


def write_json_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
