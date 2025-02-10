#!/usr/bin/python3
import json
import sys


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)

def load_from_json_file(filename):
    with open(filename, "r", encoding="utf_8") as file:
        json.load(file)

if __name__ == "__main__":
    filename = "add_item.json"
    try:
        item = load_from_json_file(filename)
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save_to_json_file(item, filename)
