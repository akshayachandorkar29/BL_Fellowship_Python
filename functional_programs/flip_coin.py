from utility import Utility

coin_object = Utility()

trials = int(input("Enter number of trials: "))
# assigning values returned by function to the variables
hp, tp = coin_object.flip_coin(trials)  # This will return tuple

