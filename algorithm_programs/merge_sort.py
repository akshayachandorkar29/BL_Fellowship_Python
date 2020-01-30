from utility import Utility

merge_object = Utility()

size = int(input("Enter size of the array: "))
arr = merge_object.list_creation(size)

print(f"Sorted Array: {merge_object.merge_sort(arr)}")

