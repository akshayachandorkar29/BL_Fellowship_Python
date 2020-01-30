"""
This is the driver function for calculating binary search trees given any number
Author : Akshaya Revaskar
Date : 17 / 01 / 2020
"""
from utility_data_structure import BinarySearchTree

bst = BinarySearchTree()
# taking user input for no. of test cases so that program can run that many times
test_cases = int(input("Enter number of test cases: "))

# calling binary count method and printing the count
for i in range(1, test_cases + 1):
    print(bst.count_binary(i))
