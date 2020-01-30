import unittest
from utility import Utility


class test_vending_machine(unittest.TestCase):

    def test_vending_machine(self):

        amount = 25000
        expect = 25
        result = Utility.vending_machine(amount)
        self.assertEqual(expect, result)

    def test_vending_machine_string_input(self):

        amount = "bcfjdshfj"
        expect = "Invalid Input!!!"
        result = Utility.vending_machine(amount)
        self.assertEqual(expect, result)

    def test_vending_machine_alphanum(self):

        amount = "bcfjdshfj6756"
        expect = "Invalid Input!!!"
        result = Utility.vending_machine(amount)
        self.assertEqual(expect, result)

    def test_vending_machine_numalpha(self):

        amount = "6756shgf"
        expect = "Invalid Input!!!"
        result = Utility.vending_machine(amount)
        self.assertEqual(expect, result)