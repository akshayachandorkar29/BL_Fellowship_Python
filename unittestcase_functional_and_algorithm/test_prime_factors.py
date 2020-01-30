import unittest
from utility import Utility


class test_prime(unittest.TestCase):

    def test_prime_fact(self):
        num = 10
        expect = [2, 5]
        result = Utility.prime_factors(num)
        self.assertEqual(expect, result)

    def test_prime_lesser_number(self):
        num = -1
        expect = False
        result = Utility.prime_factors(num)
        self.assertEqual(expect, result)
