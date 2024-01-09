#!/use/bin/python3
"""Adds an item to the files"""


import os
import sys
import json


def save_to_json_file(my_obj, filename):
    """saves the content of obj to .json file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """reads the whole files from a file"""

    with open(filename, 'r') as file:
        return (json.load(file))


if __name__ == '__main__':
    if not os.path.exists('add_item.json'):
        save_to_json_file([], 'add_item.json')

    jsoned = load_from_json_file('add_item.json')
    for i in range(1, len(sys.argv)):
        jsoned.append(sys.argv[i])

    save_to_json_file(jsoned, 'add_item.json')
