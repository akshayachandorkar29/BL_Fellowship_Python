"""
Test cases for commercial shares
Author: Akshaya Revaskar
Date: 26/01/2020
"""
import pytest
from datetime import datetime
from oops_programs.commercial import Share, StockAccount

test_share = Share("onida", 200)
test_stock = StockAccount()


def test_time_of_transaction():
    assert test_share.time_transact == datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

def test_add_shares():
    hasattr(test_stock.add_shares("nokia", 300), "name")
    hasattr(test_stock.add_shares("nokia", 300), "number")

def test_sell_shares():
    hasattr(test_stock.sell("nokia", 100), "sell_name")
    hasattr(test_stock.add_shares("nokia", 50), "sell_number")

pytest.main()