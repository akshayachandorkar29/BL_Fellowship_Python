from utility import Utility

insertion_sort_string_object = Utility()

while True:
    try:
        new_string = ""
        string = input("Enter String to Sort: ")
        string = string.strip()
        if string.isalpha() and (string.isnumeric() == False):
            new_string = (string.lower()).replace(" ", "")
        break
    except ValueError:
        print("Invalid input! Please Enter strings")

sorted_list = insertion_sort_string(new_string)
print(sorted_list)
