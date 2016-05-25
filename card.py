class Card:

    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = []

    def build_deck(self):
        for self.suit in self.suits:
            for self.card in self.cards:
                self.deck.append(self.suit + " " + self.card)
