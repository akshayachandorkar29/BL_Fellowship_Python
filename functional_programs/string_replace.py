"""

"""

from utility import Utility

string_object = Utility()

# Getting input from user
string3 = input("Enter Username: ")
string3 = string3.strip()  # removing spaces if user types any

# Calling method from utility
string = string_object.replace_string(string3)
print(string)
