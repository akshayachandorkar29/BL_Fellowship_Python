""" This file contains test cases for replacing string with regex
Author: Akshaya Revaskar
Date: 22/01/2020
"""
from oops_programs.replace_using_regex import Regex
r = Regex()

# def test_replace_string_using_regex():
#
#     assert r.replace_using_regex() == "Hello Akshaya, We have your full name as Akshaya Chandorkar in our system. \n" \
#                       "your contact number is 91­9773019523. \n" \
#                       "Please,let us know in case of any clarification Thank you BridgeLabz 23/01/2020."

def test_name_input():
    # actual = "Akshaya"
    expected="Akshaya"
    result = r.name_input()
    assert expected == result
#
# def test_full_name_input():
#     actual = "Akshaya Chandorkar"
#     expected = r.full_name_input()
#     assert actual == expected
#
# def test_phone_input():
#     actual = "9890989098"
#     expected = r.phone_input()
#     assert actual == expected
#
# def test_date_input():
#     actual = 11/12/2009
#     expected = r.date_input()
#     assert actual == expected



