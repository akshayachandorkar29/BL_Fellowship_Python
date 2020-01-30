from utility import Utility

guess_number_object = Utility()

N = int(input("Enter upper number of a range: "))
num_list = list(range(0, N+1))
print(num_list)

guess_number(num_list)