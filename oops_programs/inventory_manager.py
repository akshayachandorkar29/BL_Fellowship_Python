""" Adding items to inventory
Author: Akshaya Revaskar
Date: 27/01/2020
    TODO: add inventory in json file and calculate total price of each inventory
"""
import json


class Inventory_Manager:

    def __init__(self, json_file):  # Initialising instance variables, taking in a file to get data from json file
        self.json_file = json_file
        self.inventory = None

    def inventory_factory(self):
        """
        Method to get data from inventory file and show value of each item in inventory
        """

        with open(self.json_file, 'r') as f:
            self.inventory = json.load(f)
        for item in self.inventory["inventory"]:
            print(f"value of {item['weight']}Kg of {item['name']} is {item['weight'] * item['price_per_kg']} ")

    def add_to_inventory(self):
        """
        Method to add item to inventory and save to json file
        """
        n = int(input("Enter number of items you would like to add to inventory :\n"))
        for i in range(n):
            while True:
                try:  # Getting information about data to add to inventory json file
                    item = input("Item you would want to enter to inventory :\n")
                    weight = int(input("Enter weight of the product you are adding to inventory :\n"))
                    price = int(input("Enter cost per KG of the product "))

                except ValueError:
                    print("Please enter values for weight and price per kg")

                else:
                    break

            with open(self.json_file, 'r+') as f:  # Saving changes to json file
                data = dict()
                data['name'] = item
                data['weight'] = weight
                data['price_per_kg'] = price
                self.inventory["inventory"].append(data)
                json.dump(self.inventory, f, indent=2)


if __name__ == "__main__":
    im = Inventory_Manager("inventory_mgmt.json")
    im.inventory_factory()
    im.add_to_inventory()