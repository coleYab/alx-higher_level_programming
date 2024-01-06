#!/usr/bin/python3
"""# print square
- a function to print a square by using hash
"""


def print_square(size):
    """# print square
    a fuction to print a square from it."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#"*size)
