"""Driver code for stack
    Author : Akshaya Revaskar
    Date : 17 / 01 / 2020

    a. Desc ­> Take an Arithmetic Expression such as
    (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
    performance of operations. Ensure parentheses must appear in a balanced
    fashion.
    b. I/P ­> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
    c. Logic ­> Write a Stack Class to push open parenthesis “(“ and pop closed
    parenthesis “)”. At the End of the Expression if the Stack is Empty then the Arithmetic Expression is Balanced.
    Stack Class Methods are Stack(), push(), pop(), peak(), isEmpty(), size()
    d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.
"""
from utility_data_structure import Stack

# expression = input("Enter the expression: ")
#
expression_object = Stack()
# expression_object.balanced_paranthesis(expression)

expression_object.push(10)
expression_object.push(20)
expression_object.push(30)
expression_object.push(40)
expression_object.pop()
stack_list = expression_object.display_stack()
print(stack_list)

