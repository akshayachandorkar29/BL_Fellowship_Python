""" driver code for storing Prime numbers in 2d array
Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range. Store
the prime numbers in a 2D Array, the first dimension represents the range 0­100,
100­200, and so on. While the second dimension represents the prime numbers in
that range
Author : Akshaya Revaskar
Date : 17 / 01 / 2020
"""
from utility_data_structure import Prime

prime_object = Prime()

prime = prime_object.prime_array()

prime_array = prime_object.check_prime_range()
print(f"2d prime array is: {prime_array}")
print()

anagram_list, not_anagram_list = prime_object.prime_anagram(prime)

print(f"Prime Numbers that are Anagrams: {anagram_list}")
print()

print(f"Prime Numbers that are NOT Anagrams: {not_anagram_list}")
