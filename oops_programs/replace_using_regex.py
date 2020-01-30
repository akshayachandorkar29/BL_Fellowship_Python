"""This file contains regular expression demonstration
Author : Akshaya Revaskar
Date : 22/01/2020
TODO : replace_using_regex method will take user inputs for name, full_name, contact_number and replace original/
       message with user inputs using regex
"""

import re


class Regex:

    def __init__(self):
        pass

    def name_input(self):
        """ Method to take name as a input from user

        :return: first_name: user given name after validation is performed
        """
        try:
            name_check = re.compile(r"[^A-Za-zs.]")

            first_name = input("Please, enter your name: ")
            while name_check.search(first_name):
                print("Please enter your name correctly!")
                first_name = input("Please, enter your name: ")
            return first_name
        except Exception:
            print("Error!!!")

    def full_name_input(self):
        """ Method to take full_name as a input from user

        :return: full_name: user given name after validation is performed
        """
        try:
            full_name_check = re.compile(r"[^A-Za-zs. ]")

            full_name = input("Please, enter your full name: ")

            while full_name_check.search(full_name):
                print("Please enter your full name correctly!")
                full_name = input("Please, enter your full name: ")
            return full_name
        except Exception:
            print("Error!!!")

    def phone_input(self):
        """ Method to take phone number as a input from user

        :return: phone: user given phone after validation is performed
        """
        try:
            phone_check = re.compile(r"^[7-9][0-9]{9}")

            phone = input("Please, enter your phone: ")

            if phone_check.match(phone):
                return phone
            else:
                self.phone_input()
        except Exception:
            print("Error!!!")

    def date_input(self):
        """ Method to take date as a input from user

        :return: date: user given date after validation is performed
        """
        try:
            date_check = re.compile(r"^[0-3][0-9]/[0-3][0-9]/(?:[0-9][0-9])?[0-9][0-9]$")

            date = input("Please, enter date: ")

            if date_check.match(date):
                return date
            else:
                self.date_input()
        except Exception:
            print("Error!!!")

    def replace_using_regex(self):
        """ This method replaces a message by user given inputs

        :return: message: template after replacing
        """
        try:
            # given template
            message = "Hello <<name>>, We have your full name as <<full_name>> in our system. \n" \
                          "your contact number is 91­xxxxxxxxxx. \n" \
                          "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."

            first_name = self.name_input()
            full_name = self.full_name_input()
            phone = self.phone_input()
            date = self.date_input()

            message = re.sub("<<name>>", first_name, message)
            message = re.sub("<<full_name>>", full_name, message)
            message = re.sub("xxxxxxxxxx", phone, message)
            message = re.sub("01/01/2016", date, message)

            print(message)
            return message
        except Exception:
            print("Error!!!")


def main():
    r = Regex()  # creating object of Regex class

    r.replace_using_regex()


if __name__ == '__main__':
    main()

