#!/usr/bin/python3
"""The module to test the square model"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that will abstract the real square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square based on the inputs provided"""
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
        return {
            "id": self.id, "size": self.size,
            "x": self.x, "y": self.y
        }
