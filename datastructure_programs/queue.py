"""Driver code for Queue
Author : Akshaya Revaskar
Date : 17 / 01 / 2020

   a. Desc ­> Create a Program which creates Banking Cash Counter where people
    come in to deposit Cash and withdraw Cash. Have an input panel to add people
    to Queue to either deposit or withdraw money and dequeue the people. Maintain
    the Cash Balance.
    b. I/P ­> Panel to add People to Queue to Deposit or Withdraw Money and dequeue
    c. Logic ­> Write a Queue Class to enqueue and dequeue people to either deposit
    or withdraw money and maintain the cash balance
    d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.
"""

from utility_data_structure import Queue
queue_object = Queue()

queue_object.bank_cash_counter()
