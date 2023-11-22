# Lewis Benson
# CIS261
# DeckOfCards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, number):
        if number <= len(self.deck):
            dealt_cards = self.deck[:number]
            self.deck = self.deck[number:]
            return dealt_cards
        else:
            return None

    def count(self):
        return len(self.deck)

def main():
    deck = Deck()
    print("I have shuffled a deck of 52 cards.")
    while deck.count() > 0:
        num_cards = min(5, deck.count())
        dealt_cards = deck.deal(num_cards)
        print("\nHere are your cards:")
        for card in dealt_cards:
            print(card)
        print(f"There are {deck.count()} cards left in the deck.")
        if deck.count() > 0:
            input("Press any key to continue . . .")
        else:
            print("No more cards left in the deck.")
    input("Press any key to end the game.")

if __name__ == "__main__":
    main()
