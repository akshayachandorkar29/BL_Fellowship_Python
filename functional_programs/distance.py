from utility import Utility

distance_object = Utility()

while True:
    try:
        x = int(input("Enter x co-ordinate: "))
        y = int(input("Enter y co-ordinate: "))
        break
    except ValueError:
        print("Invalid input!!!")

print(f"distance between two points is: {distance_object.distance(x, y)}")

