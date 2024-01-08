#!/usr/bin/python3
"""a module to do some task
"""


class MyList(list):
    """MyList -> a class that inherits form a list
    This is he class to do the task
    """

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
