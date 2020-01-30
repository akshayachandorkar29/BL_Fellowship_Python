"""Deck of Cards
@Purpose: Shuffling a deck of cards and distributing it among 4 players each having 9 cards
@author: Akshaya Revaskar
@date: 25/01/2020
TODO: This programs will randomly assign 9 cards to each of 4 players and print them
"""

import random


class Deck:
    """This class contains deck of cards having suit and rank which can be shuffled and distributed
    """
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []

    def pack_of_cards(self):
        """This method creates a deck of 52 cards
        :return: self.cards: a list of cards
        """
        for i in self.suit:
            for j in self.rank:
                self.cards.append(j + " of " + i)  # Appending the possible cards in the empty list
        return self.cards

    def players_shuffle(self):
        """This method shuffles the deck of cards for 4 players and distributing 9 cards to each player
        :return: prints the cards distributed to the four players
        """
        print(f"All the possible 52 cards: {self.pack_of_cards()}")
        print()

        shuffle_cards = random.sample(self.pack_of_cards(), 36)  # 36 is the total cards needed(9*4)
        print(f"Cards after shuffling: {shuffle_cards}")

        # dividing shuffled list among 4 players
        cards_of_players = []
        cards_of_players.append(shuffle_cards[:9])
        cards_of_players.append(shuffle_cards[9:18])
        cards_of_players.append(shuffle_cards[18:27])
        cards_of_players.append(shuffle_cards[27:])

        print()
        print(f"Final Distribution of Cards among 4 players: {cards_of_players}")

        return cards_of_players


if __name__ == '__main__':
    new_deck = Deck()
    new_deck.players_shuffle()
