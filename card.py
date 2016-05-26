class Card:

    def __init__(self):
        self.suits = ["♠", "♥", "♦", "♣"]
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = []

    def build_deck(self):
        for suit in self.suits:
            for card in self.cards:
                    self.deck.append(card + " " + suit)
        return self.deck

'''
deck = Card()
deck.build_deck()
print(deck.deck)
'''

