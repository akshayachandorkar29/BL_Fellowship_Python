from utility import Utility

sum_three_object = Utility()

size = int(input("Enter size of the list: "))

created_list = sum_three_object.list_creation(size)
print(f"list is : {created_list}")

sum_three_object.sum_of_three_integers(created_list)