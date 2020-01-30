import unittest
from utility import Utility


class test_coupon(unittest.TestCase):

    def test_coupon_random(self):
        distinct_list = [1, 2, 5, 6, 9, 7, 11]

        expect = 14
        result = Utility.coupon_number(distinct_list)
        self.assertEqual(expect, result)

    def test_coupon(self):
        distinct_list = [1, 2, 5, 6, 8]

        expect = 11
        result = Utility.coupon_number(distinct_list)
        self.assertEqual(expect, result)
