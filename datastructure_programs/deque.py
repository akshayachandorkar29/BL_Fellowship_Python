""" Driver code for deque
Author : Akshaya Revaskar
Date : 17 / 01 / 2020

a. Desc ­> A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.
b. I/P ­> Take a String as an Input
c. Logic ­> The solution to this problem will use a deque to store the characters of
the string. We will process the string from left to right and add each character to
the rear of the deque.
d. O/P ­> True or False to Show if the String is Palindrome or not.
"""

from utility_data_structure import Deque
deque_object = Deque()

deque_object.add_front(10)
deque_object.add_front(20)
deque_object.add_front(30)
deque_object.remove_front()
# deque_object.add_rear()
# deque_object.add_rear()
print("DFSDfgg")
deque_object.get_deque()


# print(deque_object.palindrom_checker())
