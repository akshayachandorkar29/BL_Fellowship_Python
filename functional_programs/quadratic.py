from utility import Utility

quadratic_object = Utility()

try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of b: "))
    # 1, 3, -4
except ValueError:
    print("Invalid input!!!")

quad_tuple = quadratic_object.quadratic(a, b, c)
print(quad_tuple)

