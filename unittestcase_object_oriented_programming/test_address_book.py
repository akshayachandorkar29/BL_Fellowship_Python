""" This file contains test cases for address book problem
Author: Akshaya Revaskar
Date: 27/01/2020
"""
import pytest
from oops_programs.address_book import AddressBook

add_book = AddressBook()


def test_add_book():
    hasattr(add_book.add_person(), "first_name")
    hasattr(add_book.add_person(), "last_name")
    hasattr(add_book.add_person(), "zip")


def test_isInstance():
    print(isinstance(add_book, AddressBook))

def test_delete_attributes():
    hasattr(add_book.delete_entry(), "first_name")
    hasattr(add_book.delete_entry(), "last_name")

#
# def test_display():
#     assert add_book.display() == "file not found"
#
#
# def test_delete_entry():
#     assert add_book.delete_entry() == "data deleted!!!"


pytest.main()

