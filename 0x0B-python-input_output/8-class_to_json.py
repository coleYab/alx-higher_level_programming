#!/usr/bin/python3
"""A module that converts a class to a JSON-formatted string"""


def class_to_json(a_obj):
    """Converts a class to a JSON-formatted string"""
    def convert_value(value):
        """Convert non-string values to string representation"""
        if isinstance(value, str):
            return f"'{value}'"
        else:
            return str(value)

    dic = a_obj.__dict__
    
    # Convert key-value pairs to JSON-formatted string
    json_pairs = [f"'{key}': {convert_value(value)}" for key, value in dic.items()]

    # Construct the final JSON string
    json_string = "{" + ", ".join(json_pairs) + "}"

    return json_string
