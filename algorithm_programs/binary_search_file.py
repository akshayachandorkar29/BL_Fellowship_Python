from utility import Utility

binary_search_file_object = Utility()

try:
    file = open("binary.txt")
    file = file.read()
except FileNotFoundError:
    print("File Not Found...!!!")

file_list = list(file.split(", "))

file_list_sorted = binary_search_file_object.bubble_sort(file_list)
print(f"sorted list is : {file_list_sorted}")

key = input("Enter word to be searched: ")
key = (key.strip()).lower()
binary_search_file_object.binary_search_file(file_list_sorted, key)

