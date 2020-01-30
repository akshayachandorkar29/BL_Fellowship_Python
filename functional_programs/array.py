from utility import Utility

array_object = Utility()

outside_size = int(input("enter number of rows"))

array = []    # declaration

print("Enter elements")
for i in range(0, outside_size):   #
    array.append([(j) for j in input().split()])  # taking space separated elements

array_object.array(array)
