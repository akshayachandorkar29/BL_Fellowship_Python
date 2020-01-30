from utility import Utility

binary_object = Utility()

while True:
    try:
        num = int(input("Enter Decimal Number to be converted: "))
        break
    except ValueError:
        print("Invalid Input!!!")

print(f"Binary conversion of {num} : {binary_object.dec_to_binary(num)}")
