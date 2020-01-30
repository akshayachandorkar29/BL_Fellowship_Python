"""Commercial Data Processing
@Purpose: Maintains tracks of shares purchased as well as datetime of transaction
@author: Akshaya Revaskar
@date: 23/01/2020
"""

from datetime import datetime
from utility_data_structure import Linked_List


class Share:
    """This class is used by financial institution to keep track of customer information
    """

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.time_transact = time_transaction()


def time_transaction():
    """This method keeps track of the time of the transaction
    :return: current time
    """
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time


class StockAccount:
    """This class contains methods to buy or sell the shares"""

    def __init__(self):
        self.value = 0
        self.company_shares_list = Linked_List()
        self.stock_list = []

    def add_shares(self, name, number):
        """This method adds the shares to the existing company
        :param name: name of the company
        :param number: number of shares purchased
        :return: list of company and shares
        """
        new_share = Share(name, number)
        self.company_shares_list.insert_at_end(new_share)
        self.stock_list.append(new_share)

    def buy(self, new_name, new_number):
        """This method buys shares for the existing company or adds the company if the company doesn't exist in the list
        :param new_name: name of the company
        :param new_number: number of shares
        :return: appends the shares to the company
        """
        flag = False
        for i in self.stock_list:  # If the name exists in the stock list
            if new_name == i.name:
                self.company_shares_list.delete_item(i)
                i.number += new_number
                flag = True
                i.time_transact = time_transaction()
                self.company_shares_list.insert_at_end(i)

        if flag is False:
            new_share = Share(new_name, new_number)
            new_share.time_transact = time_transaction()
            self.stock_list.append(new_share)
            self.company_shares_list.insert_at_end(new_share)

    def sell(self, sell_name, sell_number):
        """This method sells the stocks of the company and displays the remaining stocks
        :param sell_name: name of the company
        :param sell_number: number of shares
        :return: the remaining shares of that company
        """
        flag = False
        for i in self.stock_list:
            if sell_name == i.name:
                self.company_shares_list.delete_item(i)
                i.number -= sell_number
                i.time_transact = time_transaction()
                self.company_shares_list.insert_at_end(i)
                if i.number == 0:
                    self.stock_list.remove(i)
                    self.company_shares_list.insert_at_end(i)
                flag = True
        if flag is False:
            print("\rNo such share available for sale!!!")

    def print_report(self):
        """This method displays the number of shares of the following company with the date and time of the purchase
        """
        for i in self.stock_list:
            print("\n{} shares of {} purchased at {}".format(i.number, i.name, i.time_transact))

    def save_file(self):
        """This method saves the report in the text format
        """
        file_object = open("commercial_data_final.txt", 'w')
        for i in self.stock_list:
            data = str("\n{} shares of {} purchased at {}".format(i.number, i.name, i.time_transact))
            file_object.write(data)


def main():
    csa = StockAccount()
    csa.add_shares("Samsung", 350)
    csa.add_shares("orio", 200)
    csa.buy("Samsung", 200)
    csa.print_report()
    csa.save_file()


if __name__ == "__main__":
    main()