#!/usr/bin/python3
"""This is the module to represet an integer"""


class MyInt(int):
    """Class to represent rebel from int"""
    def __eq__(self, num):
        """Returns the representationn of equal"""
        return not super().__eq__(self, num)
    
    def __ne__(self, num):
        """the represenattion of not equal"""
        return super().__eq__(self, num)
