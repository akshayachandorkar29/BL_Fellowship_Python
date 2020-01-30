""" This is the Inventory data management
Author : Akshaya Revaskar
Date : 22/01/2020
TODO : inventory method will read json file and convert it into dictionary.
       further we print the dictionary values.
"""
import json


class Inventory:

    def __init__(self):
        pass

    @staticmethod
    def inventory():
        """ Method to print json data into python string

        :return: inventory_dict : dictionary of inventory
        """
        try:
            # opening the inventory file
            with open("inventory.json") as f:
                inventory_dict = json.load(f)
            # traversing dictionary to print the values
            for key in inventory_dict:
                for value in inventory_dict[key]:
                    print(key)
                    price = 0
                    weight = 0
                    price += int(value["price"])
                    weight += int(value["weight"])
                    print("Name:", value["name"])
                    print("Price:", value["price"])
                    print("Weight:", value["weight"])
                    print()
            return inventory_dict
        except FileNotFoundError:
            print("File not found!!!")
        except Exception:
            print("Error")


if __name__ == '__main__':
    Inventory.inventory()
