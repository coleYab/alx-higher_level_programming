#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    msg = " must be a string"
    if not isinstance(first_name, str):
        raise TypeError(f"first_name{msg}")
    if not isinstance(last_name, str):
        raise TypeError(f"last_name{msg}")
    print('My name is ' + first_name.strip() + " " + last_name.strip())