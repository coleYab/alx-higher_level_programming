#!/usr/bin/python3
"""
This is the module that aims to abstract rectangle class
"""


class Rectangle:
    """This is the class to abstract the Rectangle entity"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property setter and getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property setter and getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self) -> int:
        """Calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle"""
        if self.__height * self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__height * self.__width == 0:
            return ''
        return '\n'.join([
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an integer")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be a type of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
