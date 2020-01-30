from utility import Utility

stopwatch_object = Utility()

try:
    start = int(input("Enter 1 to start the stopwatch"))
    stop = int(input("Enter 2 to stop the stopwatch"))
except ValueError:
    print("Invalid inputs...")

stopwatch_object.stopwatch(start, stop)