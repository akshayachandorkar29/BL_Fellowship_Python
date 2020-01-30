import unittest
from utility import Utility


class test_quadratic(unittest.TestCase):

    def test_quadratic_true(self):
        a = 1
        b = 3
        c = -4
        expect = (1.0, -4.0)
        result = Utility.quadratic(a, b, c)
        self.assertEqual(expect, result)

    def test_quadratic(self):
        a = 1
        b = -3
        c = 0
        expect = (3.0, 0.0)
        result = Utility.quadratic(a, b, c)
        self.assertEqual(expect, result)



