""" Adding the prime numbers that are anagrams
Author : Akshaya Revaskar
Date : 17 / 01 / 2020

Add the Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Queue using
the Linked List and Print the Anagrams from the Queue. Note no Collection Library
can be used.
"""
from utility_data_structure import Queue, Prime

prime_object = Prime()
anagram_queue_object = Queue()

prime_list = prime_object.prime_array()
anagram_list, not_anagram_list = prime_object.prime_anagram()

for ele in anagram_list:
    anagram_queue_object.enqueue(ele)

size = anagram_queue_object.size()

for element in range(0, size - 1):
    print(anagram_queue_object.dequeue())
