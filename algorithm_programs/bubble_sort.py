from utility import Utility

bubble_sort_object = Utility()

size = int(input("Enter size of the list: "))

created_list = bubble_sort_object.list_creation(size)
print(f"list is : {created_list}")

sorted_list = bubble_sort_object.bubble_sort(created_list)
print(f"Sorted List : {sorted_list}")
