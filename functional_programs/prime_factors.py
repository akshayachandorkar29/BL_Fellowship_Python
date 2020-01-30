from utility import Utility

prime_object = Utility()

num = int(input("Enter number for which prime factors to be calculated: "))
# while True:
#     try:
#         num = int(input("Enter number for which prime factors to be calculated: "))
#         break
#     except ValueError:
#         print("Wrong Input...")
#         print("Please Enter a Number")

list_prime = prime_object.prime_factors(num)
# print(result)

