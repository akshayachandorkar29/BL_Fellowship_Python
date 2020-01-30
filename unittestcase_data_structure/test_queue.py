import unittest
from utility_data_structure import Queue


class test_queue(unittest.TestCase):

    def test_enqueue(self):
        data = 1
        expect = 1
        result = Queue().enqueue(data)
        self.assertEqual(expect, result)

    def test_enqueue_string(self):
        data = "akshaya"
        expect = 'akshaya'
        result = Queue().enqueue(data)
        self.assertEqual(expect, result)

    def test_banking_problem(self):
        expect = "Invalid Input!!!"
        result = Queue().bank_cash_counter()
        self.assertAlmostEqual(expect, result)


