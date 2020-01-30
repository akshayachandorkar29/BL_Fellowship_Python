"""
This is a utility file for data structure related methods containing logic
Author : Akshaya Revaskar
Date : 17 / 01 / 2020
"""
from utility import Utility
import math

utility_object = Utility()


# =======================================Unordered_Linked_List=========================================================


class Node:
    """
    Creating a Node class with reference initially set to None
    Parameters:
        data = the value contained in the node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    """
    This is the class for the Linked List
    This class contains various methods that can be performed on the linked list
    """

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        """
        Method for inserting data at start of the linked list
        Parameters:
            data: data which is to be inserted
        """
        try:
            new_node = Node(data)  # calls Node class constructor
            new_node.next = self.head  # assigning head node as a reference to the newly added node
            self.head = new_node  # now new inserted node becomes head
            # print(new_node.data)
            return new_node.data
        except Exception:
            print("Invalid input!!!")

    def insert_at_position(self, index, data):
        """
        Method for inserting data at given position in the linked list
        Parameters:
            data: data which is to be inserted
            index: position at which data to be inserted
        """
        try:
            new_node = Node(data)
            traverse_node = self.head  # assigning value of head to a temporary variable
            if index == 0:  # if user wants to add data at the 0th position, new node will become head
                self.insert_at_start(data)
            else:
                for i in range(0, index - 1):
                    traverse_node = traverse_node.next

                new_node.next = traverse_node.next
                traverse_node.next = new_node
        except Exception:
            print("Invalid Input!!!")

    def insert_at_end(self, data):
        """
        This method adds data to the end of the linked list
        Parameters:
            data: data to be added
        """
        try:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            traverse_node = self.head
            while traverse_node.next is not None:
                traverse_node = traverse_node.next
            traverse_node.next = new_node
            return new_node.data
        except Exception:
            print("Invalid Input!!!")

    def delete_at_start(self):
        """
        This method is for deleting data at the start of the linked list
        """
        try:
            if self.head is not None:
                traverse_node = self.head
                self.head = traverse_node.next
                return traverse_node
        except Exception:
            print("Invalid Input!!!")

    def delete_at_position(self, index):
        """
        This method deletes data from given index
        Parameters:
            index: index from which data has to be deleted
        """
        try:
            traverse_node = self.head
            if index == 0:
                self.head = traverse_node.next
            else:
                # traversing until index - 1
                for i in range(0, index - 1):
                    traverse_node = traverse_node.next

                temp = traverse_node.next  # storing element to be deleted in the temporary elemet
                traverse_node.next = temp.next
        except Exception:
            print("Invalid Input!!!")

    def delete_at_end(self):
        """
        This is method to delete data from the end of the linked list
        """
        try:
            traverse_node = self.head
            previous = None
            while traverse_node.next:
                previous = traverse_node
                traverse_node = traverse_node.next

            print(previous.next.data)
            previous.next = None

        except Exception:
            print("Invalid Input!!!")

    def delete_item(self, item):
        """
        This method will search the item from the linked list and deletes if found
        :param item: item is the item to be searched
        :return: True if found
        """
        try:
            traverse_node = self.head
            previous = None

            #  checking list is empty or not
            if self.head is None:
                print("List is empty...")
            while traverse_node:

                # traversing the list and checking whether node's data matches user given data
                if traverse_node.data == item:
                    # print("item found!!!")
                    # print("Deleting...")
                    # deleting node if match found
                    temp = traverse_node
                    previous.next = temp.next
                    return True
                previous = traverse_node
                traverse_node = traverse_node.next
            print("item not found...")
        except Exception:
            print("Invalid Input!!!")

    def size_of_list(self):
        """
        This method will count the number of elements in the list
        """
        count = 0
        traverse_node = self.head
        while traverse_node.next:  # traversing till second last node
            count += 1
            traverse_node = traverse_node.next

        count += 1
        # print(count)
        return count

    def search_item(self, item):
        """
        This method will search given item in the list
        Parameter:
            item: item to be searched in the list
        :return: boolean value
        """
        try:
            traverse_node = self.head
            if self.head is None:
                print("List is empty...")
            while traverse_node:
                if traverse_node.data == item:
                    print("item found!!!")
                    return True
                traverse_node = traverse_node.next
            print("item not found...")
            return False
        except Exception:
            print("Invalid Input!!!")

    def isEmpty(self):
        """
        This method check whether the list is empty or not
        :return: Boolean value
        """
        try:
            if self.head is None:
                print("List is empty...")
                return True
            else:
                return False
        except Exception:
            print("Invalid Input!!!")

    def display(self):
        """
        This method is for displaying all the elements of linked list
        :return: linked list
        """

        traverse_node = self.head
        while traverse_node.next is not None:
            print(traverse_node.data)
            traverse_node = traverse_node.next
        print(traverse_node.data)

    def string_display(self):
        """This function adds the word to the string
        """
        try:
            current = self.head
            temp = ""
            while current:
                # print(current.data, end = ' ')
                temp = temp + current.data + " "  # it will concatenate all the words available in the linked list in /
                                                  # a single string
                current = current.next
            return temp
        except Exception:
            print("Invalid Input!!!")


a = Linked_List()  # creating instance of linked list


# =======================================Ordered Linked List===========================================================


class Ordered_Linked_List:
    """
    This is the class for the Linked List
    This class contains various methods that can be performed on the linked list
    """

    def __init__(self):
        self.head = None

    def insert_(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data > item:
                break
            previous, current = current, current.next

        new_node = Node(item)
        if previous is None:
            new_node.next, self.head = self.head, new_node
        else:
            new_node.next, previous.next = current, new_node

    def delete_item_(self, item):
        """
        This method will find the item and deletes it
        :param item: item to be deleted
        """
        Linked_List.delete_item(a, item)  # calling delete method from linked list

    def search_(self, item):
        """
        This method will search the item from the linked list
        :param item: item to be searched
        """
        Linked_List.search_item(a, item)

    def is_empty_(self):
        """
        this method will check whether the list is empty or not
        :return: boolean value
        """
        Linked_List.isEmpty(a)

    def size_(self):
        """
        This method will count the size of the linked list
        :return: integer value count
        """
        Linked_List.size_of_list(a)

    def delete_at_end_(self):
        """
        This method will delete the item from the end of the linked list
        """
        Linked_List.delete_at_end(a)

    def delete_at_pos_(self, index):
        """
        This method will delete the item at the particular position
        """
        Linked_List.delete_at_position(a, index)

    def display_(self):
        """
        This method will display the linked list
        :return: linked list
        """
        traverse_node = self.head
        while traverse_node is not None:
            print(traverse_node.data)
            traverse_node = traverse_node.next

    def string_display_(self):
        return Linked_List.string_display(a)


# ========================================== Stack ===================================================================

class Stack:
    """The following class creates an empty stack and performs various methods mentioned below
    """

    def __init__(self):
        self.items = []

    def push(self, element):
        """It adds the item to the top of the stack
        Parameters:
            element: The value to be added to the stack
        """
        self.items.append(element)
        return self.items

    def pop(self):
        """This function removes the top item from the stack and the stack is modified
        It needs no parameters
        Returns:
            The item that is removed
        """
        return self.items.pop()

    def is_empty(self):
        """This function checks whether the stack is empty or not
        Returns True if empty or else False
        """
        return self.items == []

    def peak(self):
        """This function returns the top item of the stack
        """
        return self.items[-1]

    def display_stack(self):
        """This function returns all the items of the stack
        """
        return self.items

    def get_size(self):
        """This function returns the number of items in the stack
        """
        return len(self.items)

    def balanced_paranthesis(self, expression):
        """This function takes an arithmetic expression  and checks whether the expression is balanced or not using stack
        Parameters:
            expression: an arithmetic expression taken from an user input
        Returns:
            Check Whether the expression is balanced or not
        """
        try:
            open_paren = "({[<"  # A variable containing only the open parenthesis
            closed_paren = ")}]>"  # A variable containing only the closed parenthesis

            for bracket in expression:
                if bracket in open_paren:  # Pushing the bracket if it is a Open parenthesis
                    self.push(bracket)
                elif bracket in closed_paren:
                    if self.is_empty():  # Checking if the stack is empty
                        balanced = False
                        break
                    self.pop()  # Removing the bracket if it is a Closed parenthesis
            else:
                if self.is_empty():  # Returning True if stack is empty i.e. balanced
                    balanced = True
                else:
                    balanced = False  # Returning False if the stack is not empty i.e. unbalanced
            if balanced:
                print(f"Expression {expression} is Balanced...")
            else:
                print(f"Expression {expression} is not Balanced...")
            return balanced
        except Exception:
            print("Invalid Input!!!")


# ================================================= Queue ===========================================================


class Queue:
    """This is the class for the Queue
        This class contains various methods that can be performed on the Queue
    """

    def __init__(self):
        self.head = None

    def enqueue(self, data):
        """It adds the item to the rear of the queue
            Parameters:
                data: The value to be added in the queue
        """
        Linked_List.insert_at_end(a, data)  # calling insert function from linked list
        return data

    def dequeue(self):
        """It deletes the item from the front of the queue
        """
        deleted_node = Linked_List.delete_at_start(a)  # calling delete function from linked list
        return deleted_node.data

    def isEmpty(self):
        """This function will check whether queue is empty
        :return: True if list is empty or False
        """
        Linked_List.isEmpty(a)

    def size(self):
        """This function counts size of the queue
        :return: True if queue is empty or False
        """
        return Linked_List.size_of_list(a)

    def get_queue(self):
        """This function will print the queue
        """
        return Linked_List.display(a)

    def bank_cash_counter(self):
        """This is a function where people come to deposit cash or withdraw cash
        Input: Asking individuals to deposit or withdraw the amount
        """
        try:
            # creating input panel for adding people in queue
            number_in_queue = int(input("Number of people in Queue? "))
            for i in range(1, number_in_queue + 1):
                customer_name = input(f"Please Enter Customer {i}'s' Name : \n")
                # customer_balance = float(input(f"Enter Customer {i}'s' Bank Balance : \n"))
                self.enqueue(customer_name)
            while self.isEmpty() is not True:
                cust_name = self.dequeue()
                print(f"Hello {cust_name}")
                while True:
                    print("OPTIONS...")
                    print("1 --> Deposit Cash")
                    print("2 --> Withdraw Cash")
                    print("3 --> Exit")
                    # initializing balance amount for every customer as 500
                    balance = 500
                    # Taking user inputs for the type of transaction
                    choice = int(input("Please enter your choice: "))
                    if choice == 1:
                        amount = int(input("Enter Amount to Deposit : "))
                        if amount == 0:
                            print("Enter some positive Amount!")
                        else:
                            balance += amount  # updating user's bank balance
                            print("Thank You!\nCash Deposited Successfully")
                            print(f"Your balance is: {balance}")
                    elif choice == 2:
                        amount = int(input("Enter Amount to withdraw: "))
                        if balance >= amount:  # Checking if the amount to be withdrawn is available or not
                            balance -= amount  # Subtracting the withdrawal amount from the available balance
                            print("Thank You!\nCash Withdrawal Successful")
                            print(f"Your balance is: {balance}")
                        else:
                            # If the withdrawal amount is more than the cash available
                            print("Insufficient Balance!\n")
                    elif choice == 3:
                        exit()
                    else:
                        self.bank_cash_counter()
        except Exception:
            print("Invalid Input!!!")
            return "Invalid Input!!!"


# ====================================================== Deque ======================================================


class Deque:
    """This is the class for the Deque abstract data type
        This class contains various methods that can be performed on the Deque
        """

    def __init__(self):
        self.head = None

    def add_front(self, data):
        """It adds the item to the front of the deque
            Parameters:
            data: The value to be added in the deque
        """
        Linked_List.insert_at_end(a, data)  # calling insert function from linked list
        # return data

    def add_rear(self, data):
        """It adds the item to the rear of the deque
            Parameters:
            data: The value to be added in the deque
        """
        Linked_List.insert_at_start(a, data)
        # return data

    def remove_front(self):
        """It deletes the item from the front of the deque
        """
        Linked_List.delete_at_end(a)  # calling delete function from linked list

    def remove_rear(self):
        """It deletes the item from the rear of the deque
        """
        deleted_node = Linked_List.delete_at_start(a)  # calling delete function from linked list
        return deleted_node.data

    def isEmpty(self):
        """This function will check whether queue is empty
        :return: True if deque is empty or False
        """
        return Linked_List.isEmpty(a)

    def size(self):
        """This function counts size of the queue
        :return: count : no of elements in the deque
        """
        return Linked_List.size_of_list(a)

    def get_deque(self):
        """This function will print the deque
        """
        return Linked_List.display(a)

    def palindrom_checker(self):
        """This method will check given string is palindrome or not
        :return: True if palindrome or False
        """
        # taking string from user to check is it palindrome
        string_input = input("Enter the string you want to check: ")
        for letter in string_input:
            self.add_rear(letter)  # Add characters from the string to the Deque

        string1 = ""
        length = len(string_input)
        for i in range(length):
            item = self.remove_rear()
            string1 = string1 + item

        # checking string and reverse of it are equal
        string2 = string1[::-1]

        return string1 == string2


# ====================================== Binary Search Tree ==========================================================


class NodeBinary:
    """
       Creating a NodeBinary class with left_child and right_child initially set to None
       This class will acts as a constructor for binary_search_tree class
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    """
    This class will contain all the methods to insert the nodes at appropriate positions
    """

    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        This method will insert node at the root if root is empty or at the appropriate position
        :param val: value of the node to be inserted
        """
        if self.root is None:  # To Insert Node at root
            self.root = NodeBinary(val)
        else:
            self._insert(val, self.root)  # To insert Nodes based on their Value, recursively

    def _insert(self, val, cur_node):
        """
        This method will insert the node in the BST
        :param val: value of the node to be inserted
        :param cur_node: the current node after which new node to be inserted
        """
        if val < cur_node.value:  # If value is lesser than current node, value moves towards left child
            if cur_node.left_child is None:
                cur_node.left_child = NodeBinary(val)  # Place value in left child
            else:
                self._insert(val, cur_node)
        else:
            if cur_node.right_child is None:
                cur_node.right_child = NodeBinary(
                    val)  # If value is greater than cur_node, value moves towards right child
            else:
                self._insert(val, cur_node)

    def in_order(self):
        if self.root is not None:
            self._in_order(self.root)  # calling _in_order method privately

    def _in_order(self, current_node):
        """
        This method will traverse the tree by in order traversal
        :param current_node: the current node of the tree
        """
        if current_node is not None:
            self._in_order(current_node.left_child)
            print(current_node.value)
            self._in_order(current_node.right_child)

    def factorial(self, n):
        """This method calculates the factorial of a number
        Parameters:
              n: The integer input
        Returns:
              factorial: the calculated factorial of the number n
        """
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    def count_binary(self, n):
        """
        This method will calculate no of binary trees by different formations. it is catalan formula
        :param n: number for which trees to be calculated
        :return: number of different trees for given trees
        """
        return (self.factorial(2 * n)) / (self.factorial(n + 1) * self.factorial(n))  # catalan formula


# ======================================= Prime Number 2D Array =====================================================


class Prime:
    """
    This class will contain all the methods regarding prime numbers
    """

    def prime_array(self):
        """
        This method will give list of prime numbers in range 0 to 1000
        :return: prime_list
        """
        prime_list = []

        lower = 0
        upper = 1000
        for num in range(lower, upper + 1):
            if utility_object.is_prime(num):  # calling is_prime method to check whether the number is anagaram or not
                prime_list.append(num)

        return prime_list

    def prime_anagram(self):
        """
        This method will find prime numbers from 0 to 1000 which are anagrams
        :return: anagram_list:
                        list of prime numbers which are anagrams
                 not_anagram_list:
                        list of prime numbers which are not anagrams
        """
        anagram_list = []
        not_anagram_list = []

        prime_list = self.prime_array()

        for i in range(0, len(prime_list) - 1):
            # traversing j to the whole list
            for j in range(i + 1, len(prime_list)):
                # converting numbers into strings, sorting them and checking if match found
                if utility_object.bubble_sort_string(str(prime_list[i])) == \
                        utility_object.bubble_sort_string(str(prime_list[j])):
                    anagram_list.append(prime_list[i])
                    anagram_list.append(prime_list[j])
                else:
                    not_anagram_list.append(prime_list[i])
                    not_anagram_list.append(prime_list[j])
        return anagram_list, not_anagram_list

    def check_prime_range(self):
        """
        This method will give a 2d array of prime numbers in the range 0 to 1000
        :return:
        """
        prime_list_2d = []
        lower = 0
        upper = 100
        while True:
            li = []
            for num in range(lower, upper + 1):
                x = utility_object.is_prime(num)
                if x is True:
                    li.append(num)
                if num >= upper - 1:
                    break
            prime_list_2d.append(li)
            lower = upper
            upper = upper + 100  # incrementing upper limit by 100
            if upper >= 1001:
                break
        return prime_list_2d

# ===============================================Stack using linked list==========================================


class Stack_Using_Linked_List:
    """
    This class will contain methods of stack using linked list
    """

    def __init__(self):
        self.head = None

    def push_stack(self, data):
        """
        This method will push the data into stack
        :param data: data to be pushed
        """
        Linked_List.insert_at_end(a, data)

    def pop_stack(self):
        """
        This method will pop the data from the stack
        """
        Linked_List.delete_at_end(a)

    def is_empty_stack(self):
        """
        This method will check if stack is empty
        :return: boolean value
        """
        Linked_List.isEmpty(a)

    def size_stack(self):
        """
        This method will calculate size of the stack
        :return: integer value
        """
        return Linked_List.size_of_list(a)


    def display_stack(self):
        """
        This method will display the stack
        :return:
        """
        Linked_List.display(a)










