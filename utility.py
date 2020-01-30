""" This is a Utility file which contains utility class having different methods.
    Author: Akshaya Revaskar
    Date: 09/01/2020
"""
import math
import random
import time


class Utility:
    """ This is a Utility class which contains logic performing the mentioned tasks
    """

    def __init__(self):
        pass

    @staticmethod
    def replace_string(string3):
        """
        Method to replace a string

        This method will take a given string into a variable named string1, word to be replaced in string2 and
        take username from user by which given string has to be replaced.

        :param  string3: input from user by which given string has to be replaced.
                new_string3: input from user till it become valid input
        :return: this method will return a new string
        """
        string1 = "Hello <<UserName>>, How are you?"

        # converting string into lower case
        original_string = string1.lower()

        # validating user input
        try:
            if len(string3) < 3:
                raise ValueError
            elif string3.isnumeric():
                raise TypeError
        except ValueError:
            return "length should be greater than 3!!!"
        except TypeError:
            return "Numbers are not allowed!!!"
        else:
            new_string = original_string.replace("<<username>>", string3).title()
            return new_string

    @staticmethod
    def flip():
        """
        Method to flip a coin

        This method will randomly select heads and tails based on random value generated
        :return: string "heads" or "tails"
        """
        if random.random() < 0.5:
            return "tails"
        else:
            return "heads"

    @staticmethod
    def flip_coin(trials):
        """
        Method to flip the coin

        This method will take random head or tail string from flip() method and accordingly it will increment
        head or tail variable

        :param trials: number of times user wants to flip the coin
        :return: Percentage of Heads Coming and Percentage of Tails coming
        """

        heads = 0
        tails = 0
        for i in range(trials):
            if Utility.flip() == "tails":
                tails += 1
            else:
                heads += 1

        print(f"Number of heads coming: {heads}")
        print(f"Number of tails coming: {tails}")
        hp = (heads / trials * 100)
        tp = (tails / trials * 100)

        # printing percentages of heads and tails coming
        print(f"Percentage of Heads coming: {hp}")
        print(f"Percentage of tails coming: {tp}")
        return hp, tp

    @staticmethod
    def leap_year(year):
        """
        Leap Year

        :param year: a 4 digit number as a input from user

        :return: Whether the given year is leap or not
        """
        # checking if it is 4 digit number and not a string
        try:
            if (year < 1000) and (year > 9999):
                raise ValueError
        except ValueError:
            print("number should be four digit")
            return "number should be four digit"
        else:
            # checking leap year's condition
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"{year} is LEAP YEAR")
                return True
            else:
                print(f"{year} is NOT LEAP YEAR")
                return False

    @staticmethod
    def harmonic_number(num):
        """
        Harmonic number
        Parameters:
                num: The number till which harmonic values to be calculated
        Returns:
                prints the sum of the series
        """
        try:
            if num < 0 or num is None:
                raise ValueError #Todo
        except ValueError:

            print("Number should be greater than zero")
            return "Number should be greater than zero"
        else:
            harmonic = 0
            if num > 0:
                # traversing till number given by user
                for i in range(1, num + 1):
                    # calculating harmonic addition
                    harmonic = harmonic + (1 / i)

                    print(f"1 / {i}", end="  ")
                    if i < num:
                        print("+", end="  ")

                print(f"\nAddition of harmonic series is: {harmonic}")
                return harmonic

    @staticmethod
    def prime_factors(num):
        """
        Prime Factors
        Parameters:
            num: input number to find the prime factors
        Returns:
            printing out all the prime factors of the given number
        """

        if num > 0:
            list_prime = []
            # traversing till the given number
            for i in range(2, num + 1):
                while num % i == 0:
                    print(f"{i}")
                    list_prime.append(i)
                    num = num / i

            if num > 2:
                print("number is prime number")

            return list_prime

        else:
            print("Number should be greater than zero")
            return False

    @staticmethod
    def array(array):
        """
        2D Array
        Parameters:
            array : array by getting row, columns and elements from user
        Returns:
            prints a 2 Dimensional array
        """
        for i in range(len(array)):
            print(array[i])  # printing array

    @staticmethod
    def sum_of_three_integers(new_list):
        """
        Sum of three integers adds to ZERO
        Parameters:
            new_list: number of elements in the array given by user
        Returns:
            Prints an array of distinct triplets whose sum is zero
        """
        count = 0
        size = len(new_list)

        # taking elements from array in the form of triplet
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):

                    # checking if addition of triplet is 0 or not
                    if new_list[i] + new_list[j] + new_list[k] == 0:
                        # incrementing count for counting total number of triplets
                        count += 1

                        print("Triplet Found")
                        print(f"Triplets are: {new_list[i]}  {new_list[j]}  {new_list[k]}")
        if count == 0:
            print("Triplet not found!!!")
        else:
            print(f"Number of distinct triplets are: {count}")

    @staticmethod
    def list_creation(size):
        """
        Creating Array
        Parameters:
            size : array size by user
        Returns:
            returns an array with user entered elements
        """
        new_list = []

        while len(new_list) < size:
            #  asking user to enter the number to add in an array
            item = int(input("Enter your number: "))
            new_list.append(item)

        return new_list

    @staticmethod
    def distance(x, y):
        """
        Euclidean distance
        Parameters:
            x: X coordinates as integer value
            y: Y coordinates as integer value
        Returns:
            Calculated distance from the origin
        """

        euclidean_distance = math.sqrt((x * x) + (y * y))

        return euclidean_distance

    @staticmethod
    def quadratic(a, b, c):
        """
        Roots of a quadratic equation
        Parameters:
            a, b, c: input integers
        Returns:
            prints two roots of the equation
        """
        delta = (b * b) - (4 * a * c)  # formula of calculating delta

        root1 = ((-b) + (math.sqrt(delta))) / (2 * a)  # formula of calculating first root

        root2 = ((-b) - (math.sqrt(delta))) / (2 * a)  # formula of calculating second root

        print(f"Root1 of x is: {root1}")
        print(f"Root2 of x is: {root2}")

        return root1, root2

    @staticmethod
    def wind_chill(t, v):
        """
        Windchill
        Parameters:
            t: Temperature in Fahrenheit
            v: Wind speed in miles per hour
        Returns:
            w: The effective temperature or the wind chill
        """
        try:
            if t.isalpha() or v.isalpha():
                raise ValueError("Strings are not allowed")
            elif 0 < int(t) < 50 and 3 < int(v) < 120:
                w = 35.74 + (0.6215 * int(t)) + (((0.4275 * int(t)) - 35.75) * (int(v) ** 2))
                print(f"The Effective Temperature : {w}")
                return w
            else:
                raise ValueError("Invalid Input")
        except:
            print("Enter Valid Input")
            return Exception

    @staticmethod
    def gambler(stake, goal, trials):
        """
        Gambler
        Parameters:
            stake: Starting stake
            goal: final goal the user wants to achieve
            trials: Number of times the user wants to play
        Returns:
            wins: Number of wins
            percentage of wins and losses
        """
        bets = 0
        wins = 0

        for i in range(trials):
            cash = stake

            # condition to check cash is reaching to goal or zero
            while 0 < cash < goal:
                bets += 1
                if random.random() > 0.5:
                    cash += 1
                else:
                    cash -= 1

            # condition for winning
            if cash == goal:
                wins += 1

        win_percentage = (wins / trials) * 100
        loss_percentage = ((trials - wins) / trials) * 100
        # printing number of bets, number of wins, percentage of wins as well as loss
        print(f"Bets: {bets}")
        print(f"Total Number of Wins: {wins}")
        print(f"Percentage of wins: {win_percentage}")
        print(f"Percentage of loss: {loss_percentage}")
        gambler_list = [bets, wins, win_percentage, loss_percentage]
        return gambler_list

    @staticmethod
    def coupon_number(distinct_list):
        """
        Coupon Numbers
            Parameters:
                distinct_list: distinct array from user
            Returns:
                total random numbers needed to print all the distinct numbers
        """
        # to check whether all the distinct array elements are checked or not
        visited = len(distinct_list)
        count = 0

        # traversing till all distinct array elements has been visited
        while visited > 0:

            # generating random numbers between minimum number from array and maximum number from array
            random_num = random.randrange(min(distinct_list), max(distinct_list))

            # traversing till array length
            for i in range(len(distinct_list)):

                # checking if array element and generated random number is same
                if distinct_list[i] == random_num:
                    # if condition satisfied, incrementing count and decrementing visited
                    count += 1
                    visited -= 1
                    break
            # keeping track of count of total random numbers generated
            count += 1
        return count

    @staticmethod
    def stopwatch(start, stop):
        """
        Stopwatch
            Parameters:
                start: taking user input for starting the stopwatch
                stop: taking user input for stopping the stopwatch
        Returns:
                prints the Elapsed time
        """
        start_time = 0
        stop_time = 0

        # starting the stopwatch if user enters 1
        if start == 1:
            start_time = time.time()

        # stopping the stopwatch if user enters 2
        elif stop == 2:
            stop_time = time.time()
        else:
            print("Invalid Inputs...")

        # calculating elapsed time as difference between start and stop time
        elapsed_time = start_time - stop_time
        print(f"Elapsed Time: {elapsed_time} milliseconds")
        print(f"Elapsed Time: {elapsed_time / 1000} seconds")

    @staticmethod
    def is_prime(num):
        """
        Prime Number Logic
            Parameters:
                num : number to be checked
            Returns : True or False
        """

        temp = 0
        for i in range(1, num + 1):
            if num % i == 0:
                temp += 1

        if temp == 2:
            return True
        else:
            return False

    @staticmethod
    def bubble_sort_string(string):
        """
        Bubble sort of string
            Parameters:
                string: string input from user
            Returns: Array in sorted order
        """
        string_list = list(string)
        for i in range(len(string_list)):
            for j in range(1, len(string_list) - i):

                # checking if first element is greater than second
                if string_list[j] < string_list[j - 1]:
                    # swapping elements of lists
                    temp = string_list[j - 1]
                    string_list[j - 1] = string_list[j]
                    string_list[j] = temp
        return string_list

    @staticmethod
    def bubble_sort(bubble_list):
        """
        Bubble sort of numbers
            Parameters:
                 bubble_list: array input from user
            Returns: Array in sorted order
        """
        for i in range(len(bubble_list)):
            for j in range(1, len(bubble_list) - i):

                # checking if first element is greater than second
                if bubble_list[j] < bubble_list[j - 1]:
                    # swapping elements of lists
                    temp = bubble_list[j - 1]
                    bubble_list[j - 1] = bubble_list[j]
                    bubble_list[j] = temp
        return bubble_list

    @staticmethod
    def binary_search(binary_array, key):
        """
        Binary Search
            Parameters:
                binary_array: array input from user
                key: element to find from array
            Returns: prints element found or not
        """
        # initializing low and calculating high and mid
        low = 0
        high = int(len(binary_array) - 1)
        mid = int((low + high) / 2)

        while low <= high:

            # checking whether key is greater
            if key > binary_array[mid]:
                low = int(mid + 1)
                mid = int((low + high) / 2)

            # checking whether key is smaller
            elif key < binary_array[mid]:
                high = mid - 1
                mid = int((low + high) / 2)

            # checking whether key similar to array[mid]
            elif key == binary_array[mid]:
                print(f"Search Completed...{key} Found at position {mid} !!!")
                break

        if low > high:
            print("Key not found!!!")

    @staticmethod
    def binary_search_file(file_list_sorted, key):
        """
        Binary Search
            Parameters:
                file_list_sorted: array input from user
                key: element to find from array
            Returns: prints element found or not
        """
        low = 0
        high = int(len(file_list_sorted) - 1)
        mid = int((low + high) / 2)

        while low <= high:
            if key > file_list_sorted[mid]:
                low = int(mid + 1)
                mid = int((low + high) / 2)
            elif key < file_list_sorted[mid]:
                high = mid - 1
                mid = int((low + high) / 2)
            elif key == file_list_sorted[mid]:
                print(f"Search Completed...{key} Found at position {mid} !!!")
                break

        if low > high:
            print("Key not found!!!")

    def merge_sort(self, arr):
        """
        Bubble sort of numbers
            Parameters:
                arr: array input from user
            Returns: Array in sorted order
        """
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            left_array = arr[:mid]  # Dividing the array elements
            right_array = arr[mid:]  # into 2 halves

            self.merge_sort(left_array)  # Sorting the first half
            self.merge_sort(right_array)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays l[] and r[]
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    arr[k] = left_array[i]
                    i += 1
                else:
                    arr[k] = right_array[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left_array):
                arr[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                arr[k] = right_array[j]
                j += 1
                k += 1

        return arr

    @staticmethod
    def vending_machine(amount):
        """
        Finding the fewest notes to be returned for Vending machine
            Parameters:
                amount: the integer value as user input
            Returns:
                displays count of each note and total number of notes to reach the goal
        """
        try:
            if type(amount) == str and amount.isdigit() is False:
                raise ValueError
        except ValueError:
            print("Invalid Input!!!")
            return "Invalid Input!!!"
        else:
            i = 0
            num_of_notes = 0
            amount = int(amount)

            # given array of notes
            notes_list = [1000, 500, 100, 50, 10, 5, 2, 1]

            while amount > 0:
                notes = int(amount / notes_list[i])
                rem_amount = int(amount % notes_list[i])
                print(f"{notes_list[i]} : {notes}")
                i = i + 1
                num_of_notes = num_of_notes + notes
                amount = rem_amount
            print(f"Total Number of Notes: {num_of_notes}")
            return num_of_notes

    @staticmethod
    def day_of_week(m, d, y):
        """
        Day of the Week
            Parameters:
                year, month, day: integer values as user input
            Returns:
                Prints the day of the date taken from the user
        """
        try:
            if type(m) == str and m.isdigit() is False or type(d) == str and d.isdigit() is False or type(y) == str and y.isdigit() is False:
                raise ValueError
        except ValueError:
            print("Invalid Input!!!")
            return "Invalid Input!!!"
        else:
            d = int(d)
            m = int(m)
            y = int(y)

            # if d in range(1, 32) and m in range(1, 12) and y in range(1000, 9999):
                # formulae for calculating day
            y0 = y - (14 - m) // 12
            x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
            m1 = m + 12 * ((14 - m) // 12) - 2
            d0 = (d + x + (31 * m1) // 12) % 7

            # dictionary having keys and their values
            day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
            print("day is: ", day_dict[d0-1])
            # print(f"Day is : {day_dict[d0]}")
            return day_dict[d0]
            # else:
            #     print("Enter values in range")
            #     return "Enter values in range"

    @staticmethod
    def dec_to_binary(num):
        """
        Decimal number to Binary
            Parameters:
                num: taking a number as input
            Returns:
                binary: Binary representation and binary decomposition of the number into the powers of 2
        """
        binary = 0
        i = 1

        while num > 0:
            rem = int(num % 2)
            binary = int(binary + rem * i)
            num = int(num / 2)
            i = i * 10

        return binary

    @staticmethod
    def swap_nibbles(num):
        """
        Swapping decimal number nibbles
            Parameters:
                num: taking a number as input
            Returns:
                decimal number by swapping the nibbles
        """
        return (num & 0x0F) << 4 | (num & 0xF0) >> 4

    @staticmethod
    def guess_number(num_list):
        """
        Guessing Number
            Parameters:
                num_list: input array from user
            Return:
                 number guessed by user
        """
        #  prompt user to guess the number between array range
        print(f"Think of a number between {min(num_list)} and {max(num_list)}")

        low = 0
        high = int(len(num_list) - 1)
        mid = int((low + high) / 2)

        while low <= high:
            print(f"is {num_list[mid]} your number? Press 1 for YES, Press 0 for NO")
            answer = int(input())
            if answer == 1:
                print(f"You have guessed the number : {num_list[mid]}")
                break
            elif answer == 0:
                print(f"Enter 1 if your number is between {num_list[low]} - {num_list[mid]}")
                print(f"Enter 2 if your number is between {num_list[mid + 1]} - {num_list[high]}")

                choice = int(input())
                if choice == 1:
                    high = int(mid - 1)
                    mid = int((low + high) / 2)
                if choice == 2:
                    low = int(mid + 1)
                    mid = int((low + high) / 2)
            else:
                print("Element not found")

    @staticmethod
    def insertion_sort(insertion_list):
        """
        Insertion sort of numbers
        Parameters:
            insertion_list: array input from user
        Returns: Array in sorted order
        """
        for i in range(len(insertion_list)):
            for j in range(i, 0, -1):

                # checking if first element is greater than second
                if insertion_list[j] < insertion_list[j - 1]:
                    # swapping elements of lists
                    temp = insertion_list[j - 1]
                    insertion_list[j - 1] = insertion_list[j]
                    insertion_list[j] = temp
                else:
                    break
        return insertion_list

    @staticmethod
    def insertion_sort_string(string):
        """
            Insertion sort of string
            Parameters:
                string: string input from user
            Returns: Array of string in sorted order
        """
        string_list = list(string)
        for i in range(len(string_list)):
            for j in range(i, 0, -1):

                # checking if first element is greater than second
                if string_list[j] < string_list[j - 1]:
                    # swapping elements of lists
                    temp = string_list[j]
                    string_list[j] = string_list[j - 1]
                    string_list[j - 1] = temp
                else:
                    break
        return string_list

    @staticmethod
    def is_palindrome(prime_array):
        palindrome_array = []
        for i in range(len(prime_array)):
            temp = prime_array[i]
            reverse_number = 0
            while prime_array[i] > 0:
                rem = prime_array[i] % 10
                reverse_number = reverse_number * 10 + rem
                prime_array[i] = int(prime_array[i] / 10)

            if reverse_number == temp:
                palindrome_array.append(temp)

        print(f"Palindrome Array: {palindrome_array}")
        return palindrome_array

    @staticmethod
    def anagram(string1, string2):
        """
        Anagram Detection
            Parameters:
                string1: string as input from the user
                string2: string as input from the user
            Returns:
                Prints whether strings are anagrams or not
        """
        # removing extra space from both the ends
        string1 = string1.strip()
        string2 = string2.strip()

        # converting into lower case and removing in between spaces if any
        new_string1 = (string1.lower()).replace(" ", "")
        new_string2 = (string2.lower()).replace(" ", "")

        # checking if string has alphabets and they are non numeric
        if new_string1.isalpha() and new_string2.isalpha() or new_string1.isnumeric() and new_string2.isnumeric():

            sorted_string1 = ""
            sorted_string2 = ""

            # sorting strings according alphabetical order
            sorted_string_list1 = Utility.insertion_sort_string(new_string1)
            sorted_string_list2 = Utility.insertion_sort_string(new_string2)

            # checking if length of both the strings is equal
            if len(new_string1) == len(new_string2):

                # checking if both the strings are equal
                if sorted_string1.join(sorted_string_list1) == sorted_string2.join(sorted_string_list2):
                    print("Strings are ANAGRAMS!!!")
                    return "Strings are ANAGRAMS!!!"
                else:
                    print("Strings are NOT ANAGRAMS!!!")
                    return "Strings are NOT ANAGRAMS!!!"
            else:
                print("Length is not equal, Not ANAGRAMS")
                return "Length is not equal, Not ANAGRAMS"
        else:
            print("Invalid Input!!! Please Enter String")
            return "Invalid Input!!! Please Enter String"

    @staticmethod
    def prime_number(lower, upper):
        """
        Prime Number
            Parameters:
                lower: lower range
                upper: upper range
            Return:
                 prime_list: array of prime numbers between given range
        """
        prime_list = []

        for num in range(lower, upper + 1):
            if Utility.is_prime(num):
                print(num)
                prime_list.append(num)

        print(f"Prime Numbers Between {lower} and {upper} are: {prime_list}")

        Utility.is_palindrome(prime_list)
        return prime_list

    @staticmethod
    def tic_tac_toe_game():
        """
        Tic-tac-toe game
        Parameters:
            Taking user input for player1 and generating random number for computer to mark X and O
        Returns:
            Prints the board after every step until the result
        """

        def tic_tac_toe():
            board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            end = False
            # Possible winning outcomes
            win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

            # Printing the board
            def print_board():
                temp = 0
                for i in range(3):
                    for j in range(3):
                        print(board[temp], end=" ")
                        temp += 1
                    print()
                print()

            # Asking Player1 to choose the position to fill up the value and then printing the board
            def player1():
                number = choose_number()
                if board[number] == 'X' or board[number] == 'O':
                    print('\n Value already there')
                    player1()
                else:
                    board[number] = 'X'

            # Asking 2 to choose the position to fill up the value and then printing the board
            def player2():
                number = choose_number()
                if board[number] == 'X' or board[number] == 'O':
                    print('\n Value already there')  # if the values are already present then ask again to play
                    player2()
                else:
                    board[number] = 'O'

            def choose_number():
                # Ensuring that the input value is an integer value displaying on the board
                while True:
                    try:
                        a = int(input("Enter position where you want to place your symbol: "))
                        if a in board:
                            return a
                        else:
                            print('\nValue Already There!')
                    except ValueError:
                        print('Not a number. Retry')

            def game_over():
                # if the winning combination is satisfied, then the respective player wins
                count = 0
                for i, j, k in win_combinations:
                    if board[i] == board[j] == board[k] == 'X':
                        print('Congratulations!\n')
                        print('Player 1 Wins!\n')
                        return True
                    if board[i] == board[j] == board[k] == 'O':
                        print('Congratulations!\n')
                        print('Player 2 Wins!\n')
                        return True

                # Printing tie if all the cells are full with no win combinations
                for i in range(9):
                    if board[i] == 'X' or board[i] == 'O':
                        count += 1
                        if count == 9:
                            print('Its a tie between you....\n')
                            return True

            while not end:
                print_board()
                end = game_over()
                if end is True:
                    break
                print("Player1's Turn")
                player1()
                print()
                print_board()

                end = game_over()
                if end:
                    break
                print("Player2's Turn...")
                player2()
                print()

        while True:
            tic_tac_toe()
            if input('Play Again(y/n)\n') != 'y':  # Asking whether the users want to play again
                print("Wrong Choice!!!")
                break

