#!/usr/bin/python3
"""A module to test the whole base module"""


from models import base
import unittest


class TestBase(unittest.TestCase):
    """A class to test all the module"""

    def setUp(self):
        """This is the tool to execute before the test"""
        self.obj1 = base.Base(1)
        self.obj2 = base.Base(12)
        self.obj3 = base.Base(13)

    def test_obj1(self):
        """test obj1 tests the base class"""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 12)
        self.assertEqual(self.obj3.id, 13)

    def test_loop(self):
        """test loop tests the base class"""
        for i in range(0, 7):
            obj = base.Base(i)
            self.assertEqual(obj.id, i)

    def test_val(self):
        """test val tests the base class"""
        for i in range(4):
            obj = base.Base()
            self.assertEqual(obj.id, 17 + i)
