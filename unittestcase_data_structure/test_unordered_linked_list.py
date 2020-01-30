import unittest
from utility_data_structure import Linked_List


class test_linked_list(unittest.TestCase):

    def test_insert_at_start(self):
        data = 1
        expect = 1
        result = Linked_List().insert_at_start(data)
        self.assertEqual(expect, result)

    def test_insert_at_start_string(self):
        data = "asd"
        expect = "asd"
        result = Linked_List().insert_at_start(data)
        self.assertEqual(expect, result)

    def test_isEmpty(self):
        expect = True
        result = Linked_List().isEmpty()
        self.assertEqual(expect, result)




