""" This file contains test cases for inventory management using json
Author: Akshaya Revaskar
Date: 22/01/2020
"""
from oops_programs import json_inventory_data_mgmt


# testing function
def test_inventory_function_creation():
    assert json_inventory_data_mgmt.Inventory.inventory() == None


#testing file is there or not
def test_inventory_file_not_found():
    assert json_inventory_data_mgmt.Inventory.inventory() == None




