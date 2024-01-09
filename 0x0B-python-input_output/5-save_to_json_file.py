#!/usr/bin/python3
"""The module to save content to json file"""


import json


def save_to_json_file(my_obj, filename):
    """saves the content of obj to .json file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
