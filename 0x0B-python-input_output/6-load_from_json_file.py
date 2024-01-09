#!/usr/bin/python3
"""A module to read from a json file"""


import json


def load_from_json_file(filename):
    """reads the whole files from a file"""

    with open(filename, 'r') as file:
        return (json.load(file))
