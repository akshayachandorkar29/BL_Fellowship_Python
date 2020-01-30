"""
Test cases for deck of cards
Author: Akshaya Revaskar
Date: 26/01/2020
"""
import pytest
from oops_programs.deck_of_cards import Deck

deck_test = Deck()


def test_type():
    hasattr(deck_test.pack_of_cards(), "cards")
    hasattr(deck_test.players_shuffle(), "shuffle_cards")
    hasattr(deck_test.players_shuffle(), "first, second, third, fourth")


def test_pack():
    assert len(deck_test.suit) == 4
    assert len(deck_test.rank) == 13
