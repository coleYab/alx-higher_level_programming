#!/usr/bin/python3
def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ('Betty School, ' * (magic_string.counter - 1)) + 'Betty School'
