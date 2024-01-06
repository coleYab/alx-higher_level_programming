#!/usr/bin/python3
"""# A module that contains a function to say your name
- Say my name: says your name.
"""


def say_my_name(first_name, last_name=""):
    """# say my name
    - first name and last name says your name"""

    msg = " must be a string"
    if not isinstance(first_name, str):
        raise TypeError(f"first_name{msg}")
    if not isinstance(last_name, str):
        raise TypeError(f"last_name{msg}")
    print('My name is ' + first_name.strip() + " " + last_name.strip())
