import unittest

from utility import Utility


class replace_string(unittest.TestCase):

    def test_string_length(self):
        string3 = "Ak"
        expect = "length should be greater than 3!!!"
        result = Utility().replace_string(string3)
        self.assertEqual(expect, result)

    def test_string(self):
        string3 = "Akshaya"
        expect = "Hello Akshaya, How Are You?"
        result = Utility().replace_string(string3)
        self.assertEqual(expect, result)

    def test_string_number(self):
        string3 = 1234
        expect = "Numbers are not allowed!!!"
        result = Utility.replace_string(string3)
        self.assertEqual(expect, result)

    def test_string_alnum(self):
        string3 = "akshaya1234"
        expect = "Hello Akshaya1234, How Are You?"
        result = Utility().replace_string(string3)
        self.assertEqual(expect, result)



