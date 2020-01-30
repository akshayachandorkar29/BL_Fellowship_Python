from utility import Utility

insertion_sort_object = Utility()

size = int(input("Enter size of the list: "))

created_list = insertion_sort_object.list_creation(size)
print(f"list is : {created_list}")

sorted_list = insertion_sort(created_list)
print(f"Sorted List : {sorted_list}")
