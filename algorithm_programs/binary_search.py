from utility import Utility

binary_search_object = Utility()

size = int(input("Enter size of the list: "))

created_list = binary_search_object.list_creation(size)

# new_created_list = created_list.sort()
print(f"list is : {created_list}")
sorted_list = binary_search_object.bubble_sort(created_list)
print(f"sorted list is : {created_list}")

key = int(input("Enter key that you want to search: "))

binary_search_object.binary_search(created_list, key)

