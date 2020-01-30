import unittest
from utility import Utility

class test_leap_year(unittest.TestCase):

    def test_leap_2015(self):
        year = 2015
        expect = False
        result = Utility().leap_year(year)
        self.assertEqual(expect, result)

    def test_leap_2016(self):
        year = 2016
        expect = True
        result = Utility().leap_year(year)
        self.assertEqual(expect, result)

    def test_leap_not_four_digit(self):
        year = 201
        expect = False
        result = Utility().leap_year(year)
        self.assertEqual(expect, result)




