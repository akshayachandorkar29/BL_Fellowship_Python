import unittest
from utility import Utility


class test_wind_chill(unittest.TestCase):

    def test_windchill(self):
        t = 25
        v = 65

        expect = -105837.785
        result = Utility.wind_chill(t, v)
        self.assertEqual(expect, result)

    def test_windchill_wrong_inputs(self):
        t = 55
        v = 65

        expect = Exception
        result = Utility.wind_chill(t, v)
        self.assertEqual(expect, result)

    def test_windchill_string_inputs(self):
        t = "t"
        v = "v"

        expect = Exception
        result = Utility.wind_chill(t, v)
        self.assertEqual(expect, result)



