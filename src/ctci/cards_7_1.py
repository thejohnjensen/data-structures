"""Create a deck of cards and the game blackjack."""
from random import randint


class Deck(object):
    """
    Create deck of cards object.

    Methods:
        shuffle
        draw card
        check if a card has been played
    """

    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    hand = []

    def __init__(self):
        """."""
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))

    def shuffle(self):
        """."""
        next_card = len(self.deck) - 1
        for card in self.deck:
            rand_int = randint(0, next_card)
            rand_swap = self.deck[rand_int]
            temp = self.deck[next_card]
            self.deck[next_card] = rand_swap
            self.deck[rand_int] = temp
            next_card -= 1

    def draw(self):
        """."""
        card = (self.deck.pop())
        return card

    def discard(self):
        """."""
        self.hand = []


class Card(object):
    """
    Card object.

    Input:
        suit
        value
    """

    def __init__(self, suit, value):
        """."""
        self.suit = suit
        self.value = value

    def __repr__(self):
        """."""
        return '{} of {}'.format(self.value, self.suit)


class BlackJack(Deck):
    """."""

    def __init__(self):
        super(BlackJack, self).__init__()
        self.shuffle()
        print('Welcome to my black jack table! \n\
                You\'ll be playing against the computer.')

        self.computer_hand = []

    def deal(self):
        self.hand.append(self.draw())
        self.computer_hand.append(self.draw())
        self.hand.append(self.draw())
        self.computer_hand.append(self.draw())
        print('Your hand is {}, {}'.format(self.hand[0],self.hand[1]))
        print('The computer is showing {}, {}'.format(self.computer_hand[0],self.computer_hand[1]))

    def hit(self):
        self.hand.append(self.draw())
        return self.hand

    def stay(self):
        self.computer_hand.append(self.draw())
        return self.computer_hand