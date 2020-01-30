import unittest
from utility import Utility


class test_gambler(unittest.TestCase):

    def test_gambler(self):
        stake = 1000
        goal = 1500
        trials = 20

        expect = [10084744, 10, 50.0, 50.0]
        result = Utility.gambler(stake, goal, trials)
        self.assertEqual(expect, result)

    def test_gambler_different(self):
        stake = 300
        goal = 350
        trials = 25

        expect = [276336, 23, 92.0, 8.0]
        result = Utility.gambler(stake, goal, trials)
        self.assertEqual(expect, result)


