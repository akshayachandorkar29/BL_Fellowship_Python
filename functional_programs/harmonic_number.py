from utility import Utility

harmonic_object = Utility()

num = int(input("Enter a number till which harmonic series to be calculated: "))

# try:
#     num = int(input("Enter a number till which harmonic series to be calculated: "))
# except ValueError:
#     print("Invalid Input")

# calling the method
harmonic = harmonic_object.harmonic_number(num)
