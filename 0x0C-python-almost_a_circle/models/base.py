#!/usr/bin/python3
"""Module Name - base.py
A module that contains the base class
"""


import turtle
import csv
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
        """Converts a file to a json string"""
        if list_dictionaries is None:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """It will save the list to the file"""
        with open(f"{cls.__name__}.json", 'w') as f:
            str_jsoned = ''
            if list_objs is None:
                str_jsoned = '[]'
            else:
                jsoned = [i.to_dictionary() for i in list_objs]
                str_jsoned = cls.to_json_string(jsoned)
            f.write(str_jsoned)

    def from_json_string(json_string):
        """reads from json string an convert it to a list"""
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("red")
        turt.pensize(12)
        turt.shape("turtle")

        turt.color("black")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width * 2)
                turt.left(90)
                turt.forward(rect.height * 2)
                turt.left(90)
            turt.hideturtle()

        turt.color("black")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width * 2)
                turt.left(90)
                turt.forward(sq.height * 2)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
