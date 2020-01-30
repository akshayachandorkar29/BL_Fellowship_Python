from utility import Utility

day_object = Utility()

d = input("Enter Date: ")
m = input("Enter Month (1 for January, 2 for February...) : ")
y = input("Enter Year: ")

day_object.day_of_week(d, m, y)
