#!/usr/bin/python3
"""
Adds two numbers and returns the result.

Parameters:
- num1 (int or float): The first number to be added.
- num2 (int or float): The second number to be added.

Returns:
int or float: The sum of num1 and num2.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Adds two numbers and returns the result.

    Parameters:
    - num1 (int or float): The first number to be added.
    - num2 (int or float): The second number to be added.

    Returns:
    int or float: The sum of num1 and num2.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Adds two numbers and returns the result.

        Parameters:
        - num1 (int or float): The first number to be added.
        - num2 (int or float): The second number to be added.

        Returns:
        int or float: The sum of num1 and num2.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Adds two numbers and returns the result.

        Parameters:
        - num1 (int or float): The first number to be added.
        - num2 (int or float): The second number to be added.

        Returns:
        int or float: The sum of num1 and num2.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Adds two numbers and returns the result.

        Parameters:
        - num1 (int or float): The first number to be added.
        - num2 (int or float): The second number to be added.

        Returns:
        int or float: The sum of num1 and num2.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Adds two numbers and returns the result.

        Parameters:
        - num1 (int or float): The first number to be added.
        - num2 (int or float): The second number to be added.

        Returns:
        int or float: The sum of num1 and num2.
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Adds two numbers and returns the result.

        Parameters:
        - num1 (int or float): The first number to be added.
        - num2 (int or float): The second number to be added.

        Returns:
        int or float: The sum of num1 and num2.
        """
        return {
            "id": self.id, "size": self.size,
            "x": self.x, "y": self.y
        }
