import unittest
from utility import Utility


class test_anagram(unittest.TestCase):

    def test_anagram_two_equal(self):
        string1 = "earth"
        string2 = "heart"
        expect = "Strings are ANAGRAMS!!!"
        result = Utility.anagram(string1, string2)
        self.assertEqual(expect, result)

    def test_anagram_different(self):
        string1 = "earth"
        string2 = "hrsdt"
        expect = "Strings are NOT ANAGRAMS!!!"
        result = Utility.anagram(string1, string2)
        self.assertEqual(expect, result)

    def test_anagram_diff_length(self):
        string1 = "earth"
        string2 = "hearterg"
        expect = "Length is not equal, Not ANAGRAMS"
        result = Utility.anagram(string1, string2)
        self.assertEqual(expect, result)

    def test_anagram_space_at_ends(self):
        string1 = "earth   "
        string2 = "   heart   "
        expect = "Strings are ANAGRAMS!!!"
        result = Utility.anagram(string1, string2)
        self.assertEqual(expect, result)

    def test_anagram_space_in_between(self):
        string1 = "hitler woman"
        string2 = "mother in law"
        expect = "Strings are ANAGRAMS!!!"
        result = Utility.anagram(string1, string2)
        self.assertEqual(expect, result)

    def test_anagram_different_cases(self):
        string1 = "EARTH"
        string2 = "Heart"
        expect = "Strings are ANAGRAMS!!!"
        result = Utility.anagram(string1, string2)
        self.assertEqual(expect, result)
