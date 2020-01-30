""" This is the stock report management
Author : Akshaya Revaskar
Date : 22/01/2020
TODO : stock report method will read json file and convert it into dictionary.
       further we print the dictionary values.
"""

import json

class Stock:

    def __init__(self):
        self.stock_dict = []

    @staticmethod
    def stock_report():
        """ Method to print json data into python string

        :return: stock_dict : dictionary of stock
        """
        try:
            # opening the stock inventory file
            with open("stock_inventory.json") as f:
                stock_dict = json.load(f)
            # traversing dictionary to print the values
            for key in stock_dict:
                for value in stock_dict[key]:
                    print(key)
                    no_of_shares = 0
                    share_price = 0
                    no_of_shares += int(value["no_of_shares"])
                    share_price += int(value["share_price"])
                    print("Stock_name:", value["stock_name"])
                    print("Share_Price:", value["share_price"])
                    print("No_of_Shares:", value["no_of_shares"])
                    print(f"Value of stock: {share_price * no_of_shares}")
                    print()
            return stock_dict
        except FileNotFoundError:
            print("File not found!!!")
        except Exception:
            print("Error")


if __name__ == '__main__':
    Stock.stock_report()