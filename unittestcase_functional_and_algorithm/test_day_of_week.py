import unittest
from utility import Utility


class test_day_of_week(unittest.TestCase):

    def test_day_of_week(self):

        d = 15
        m = 4
        y = 1993
        expect = "Thursday"
        result = Utility.day_of_week(m, d, y)
        self.assertEqual(expect, result)

    def test_day_of_week_one_string_input(self):

        d = "sgd"
        m = 4
        y = 1993
        expect = "Invalid Input!!!"
        result = Utility.day_of_week(m, d, y)
        self.assertEqual(expect, result)

    def test_day_of_week_two_string_input(self):

        d = "sgd"
        m = "dfd"
        y = 1993
        expect = "Invalid Input!!!"
        result = Utility.day_of_week(m, d, y)
        self.assertEqual(expect, result)

    def test_day_of_week_all_string_input(self):

        d = "sgd"
        m = "ixsd"
        y = "mkuhhb"
        expect = "Invalid Input!!!"
        result = Utility.day_of_week(m, d, y)
        self.assertEqual(expect, result)