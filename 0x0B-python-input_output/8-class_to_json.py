#!/usr/bin/python3
"""A module that converts a class to a JSON-formatted string"""


def class_to_json(a_obj):
    """Converts a class to a JSON-formatted string"""

    return a_obj.__dict__
