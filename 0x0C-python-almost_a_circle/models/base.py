#!/usr/bin/python3
"""Module Name - base.py
A module that contains the base class
"""


import os
import json


class Base:
    """A base class for all the classes that comes after it
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Method
        args:
            - self - the class instance its self.
            - id - unique identifier for the instances
        return: none
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", 'w') as f:
            str_jsoned = ''
            if list_objs is None:
                str_jsoned = '[]'
            else:
                jsoned = [i.to_dictionary() for i in list_objs]
                str_jsoned = cls.to_json_string(jsoned)
            f.write(str_jsoned)

    def from_json_string(json_string):
        json_list = []
        if json_string:
            json_list = json.loads(json_string)

        return json_list


    @classmethod
    def create(cls, **dictionary):
        """The tool to do this """
        obj_sq = cls(1) if cls.__name__ == 'Square' else cls(1, 3)
        obj_sq.update(**dictionary)
        return obj_sq

    @classmethod
    def load_from_file(cls):
        """A functio to load from file and returns """
        if os.path.exists(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", 'r') as file:
                loaded = list(json.load(file))
                return loaded[:]
        else:
            return []
