from utility import Utility

windchill_object = Utility()

t = input("Enter value of temperature(0>t>50)")
v = input("Enter value of wind speed(3>v>120)")


w = windchill_object.wind_chill(t, v)
