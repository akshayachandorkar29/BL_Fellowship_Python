import unittest
from utility_data_structure import Stack

class test_stack(unittest.TestCase):

    def test_push(self):
        data = 1
        expect = [1]
        result = Stack().push(data)
        self.assertEqual(expect, result)

    def test_push_string(self):
        data = "akshaya"
        expect = ['akshaya']
        result = Stack().push(data)
        self.assertEqual(expect, result)

    def test_expression(self):
        expression = "(a+b)"
        expect = True
        result = Stack().balanced_paranthesis(expression)
        self.assertEqual(expect, result)

    def test_null_expression(self):
        expression = ""
        expect = True
        result = Stack().balanced_paranthesis(expression)
        self.assertEqual(expect, result)

