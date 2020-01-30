"""driver code for anagram of prime numbers using stack
Author : Akshaya Revaskar
Date : 17 / 01 / 2020

Add the Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Stack using
the Linked List and Print the Anagrams in the Reverse Order. Note no Collection
Library can be used.
"""

from utility_data_structure import Stack_Using_Linked_List, Prime

prime_object = Prime()
my_stack = Stack_Using_Linked_List()

prime_list = prime_object.prime_array()
anagram_list, not_anagram_list = prime_object.prime_anagram()

for element in anagram_list:
    my_stack.push_stack(element)

size = my_stack.size_stack()

print("Reverse Anagram List: ")
for element in range(0, size - 1):
    my_stack.pop_stack()



