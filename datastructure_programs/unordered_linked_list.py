"""Driver code for Linked List
   all the linked list operations have performed
   Author : Akshaya Revaskar
    Date : 17 / 01 / 2020

    a. Desc ­> Read the Text from a file, split it into words and arrange it as Linked List.
    Take a user input to search a Word in the List. If the Word is not found then add it
    to the list, and if it found then remove the word from the List. In the end save the
    list into a file
    b. I/P ­> Read from file the list of Words and take user input to search a Text
    c. Logic ­> Create a Unordered Linked List. The Basic Building Block is the Node
    Object. Each node object must hold at least two pieces of information. One ref to
    the data field and second the ref to the next node object.
    d. O/P ­> The List of Words to a File.
"""
from utility_data_structure import Linked_List

unordered_linked_list = Linked_List()

# file = open('', 'r')
# contents = file.read().split()
# for word in contents:
#     unordered_linked_list.insert_at_start(word)
#
# unordered_linked_list.display()

# opening the text file
with open('unordered_list_input.txt', 'r') as f:
    for line in f:
        for word in line.split():
            unordered_linked_list.insert_at_end(word)  # reading word from file and inserting in the linked list

# display the linked list
print("list is: ")
unordered_linked_list.display()

# Updated Linked list is stored in the file
file = open("unordered_list_output.txt", 'w+')
a = unordered_linked_list.string_display()

file.write(a)
file.close()

#
# # print("File created with filename unordered_list_output.txt")
#
# unordered_linked_list.insert_at_end(10)
# unordered_linked_list.insert_at_end(20)
# unordered_linked_list.insert_at_end(30)
# unordered_linked_list.insert_at_end(40)
# unordered_linked_list.insert_at_end(50)
# unordered_linked_list.insert_at_end(60)
# unordered_linked_list.insert_at_end(70)
# unordered_linked_list.insert_at_end(80)
# # unordered_linked_list.display()
#
# unordered_linked_list.insert_at_position(4, 100)
#
# # unordered_linked_list.search_item(30)
# # unordered_linked_list.delete_at_end()
# # unordered_linked_list.delete_at_end()
# # unordered_linked_list.delete_at_end()
#
#
#
# print('kl;jkl')
# print(unordered_linked_list.size_of_list())
# unordered_linked_list.display()
