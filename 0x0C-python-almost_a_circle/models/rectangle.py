#!/usr/bin/python3
"""A class named rectagle that inherits from base"""


Base = __import__('base').Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle Class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property setter and geter for the values"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property setter and geter for the values"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property setter and geter for the values"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property setter and geter for the values"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A method to calculate the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """A method to display itsself"""
        pre_msg = '\n' * self.__y
        msg = ''.join((' ' * self.__x) + '#' * self.__width + '\n')
        print(pre_msg + (msg * self.__height), end='')

    def __str__(self):
        """Method to display the string represetation of my class"""
        my_str1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        return (f"{my_str1} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates the instances by themselves"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for keys, value in kwargs.items():
                setattr(self, keys, value)

    def to_dictionary(self):
        """Converts the class to a dictionary"""
        return {
            "id": self.id, "width": self.width,
            "height": self.height, "x": self.x,
            "y": self.y
        }
