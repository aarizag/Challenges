"""
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array
using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __gt__(self, other):
        order = {
            "spade": {"heart", "diamond", "club"},
            "club": {"heart", "diamond"},
            "diamond": {"heart"},
            "heart": {}
        }
        return self.number > other.number if self.number != other.number else\
            other.suit in order[self.suit]

    def __str__(self):
        m = {11: "J", 12: "Q", 13: "K"}
        return f"{self.suit}{self.number if self.number < 11 else m[self.number]}"


def gen_deck():
    deck = []
    for s in ["S", "C", "D", "H"]:
        for i in range(1,14):
            deck.append(Card(i, s))
    return deck


def print_deck(deck):
    suit = ""
    for c in deck:
        if c.suit != suit:
            suit = c.suit
            print()
        print(c, end=" ")


def rand_k(k):
    return randint(0, k)


def shuffle(deck):
    # deck = deck.copy()
    for i in range(len(deck)):
        r = rand_k(len(deck) - 1)
        deck[i], deck[r] = deck[r], deck[i]
    return deck


d = gen_deck()
print("fresh")
print_deck(d)
shuffle(d)
print("\n\nshuffled")
print_deck(d)