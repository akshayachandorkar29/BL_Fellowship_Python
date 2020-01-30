import unittest
from utility import Utility


class harmonic(unittest.TestCase):

    def test_harmonic_proper(self):
        num = 5
        expect = 2.283333333333333
        result = Utility().harmonic_number(num)
        self.assertEqual(expect, result)

    def test_harmonic_string(self):
        num = "hcfgbdfh"
        expect = ValueError
        result = Utility().harmonic_number(num)
        self.assertEqual(expect, result)

    def test_harmonic_lesser_number(self):
        num = -1
        expect = "Number should be greater than zero"
        result = Utility().harmonic_number(num)
        self.assertEqual(expect, result)
