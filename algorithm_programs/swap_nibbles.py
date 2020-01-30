from utility import Utility

swap_object = Utility()

while True:
    try:
        num = int(input("Enter Decimal Number to swap its nibbles: "))
        break
    except ValueError:
        print("Invalid Input!!!")

print(f"Swapped nibbles of {num} : {swap_object.swap_nibbles(num)}")
