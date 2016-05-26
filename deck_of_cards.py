from card import Card
from random import shuffle
from random import choice


class DeckOfCards:

    def __init__(self):
        self.deck = Card().build_deck()
        self.shuffle = []
        self.hand = []
        self.dealt_card = ""

    def shuffle_deck(self):
        self.deck = [[i] for i in range(52)]
        self.shuffle = shuffle(self.deck)
        return self.shuffle

    def deal_hand(self, hide=False):
        if hide == False:
            for card in self.deck:
                self.dealt_card = choice(self.deck)
            return self.dealt_card
        else:
            return " _ "

deck = DeckOfCards()
deck.shuffle_deck()
deck.deal_hand()
print(deck.dealt_card)
