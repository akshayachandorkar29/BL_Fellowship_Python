"""Arranging numbers in the ordered linked list
Author : Akshaya Revaskar
Date : 17 / 01 / 2020
a. Desc ­> Read .a List of Numbers from a file and arrange it ascending Order in a
Linked List. Take user input for a number, if found then pop the number out of the
list else insert the number in appropriate position
b. I/P ­> Read from file the list of Numbers and take user input for a new number
c. Logic ­> Create a Ordered Linked List having Numbers in ascending order.
d. O/P ­> The List of Numbers to a File.
"""
from utility_data_structure import Ordered_Linked_List

ordered_linked_list = Ordered_Linked_List()

# ordered_linked_list.insert_(20)
# ordered_linked_list.insert_(-3)
# ordered_linked_list.insert_(-5)
# ordered_linked_list.insert_(0)
# ordered_linked_list.insert_(3000)
# ordered_linked_list.display_()










# # number = int(input("Enter number to be searched"))
#
# opening the text file
with open('ordered_list_input.txt', 'r') as f:
    for line in f:
        for number in line.split():
            ordered_linked_list.insert_(number)  # reading number from file and inserting in the linked list

# display the linked list
print("list is: ")
ordered_linked_list.display_()
#
# # Updated Linked list is stored in the file
# file = open("ordered_list_output.txt", 'w+')
# a = ordered_linked_list.string_display_()
#
# file.write(a)
# file.close()
#
# print("File created with filename ordered_list_output.txt")
