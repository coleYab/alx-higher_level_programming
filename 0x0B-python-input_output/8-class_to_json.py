#!/usr/bin/python3
"""A module that convert a class to a string"""


import json


def class_to_json(a_obj):
    """Converts a class to an object"""

    return json.dumps(a_obj.__dict__)
