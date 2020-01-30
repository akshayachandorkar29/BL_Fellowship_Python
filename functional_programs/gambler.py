from utility import Utility

gambler_object = Utility()

while True:
    try:
        stake = int(input("Enter Stake: "))
        goal = int(input("Enter Goal: "))
        trials = int(input("Enter number of times program should run: "))
        break
    except ValueError:
        print("You might have entered invalid inputs...")

gambler = gambler_object.gambler(stake, goal, trials)

