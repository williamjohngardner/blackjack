from deck_of_cards import DeckOfCards


class Hand:

    def __init__(self):
        self.card = DeckOfCards()
        self.card.deal_hand()

    def deal(self, hide=False):
        if hide == False:
            return self.card.dealt_card
        else:
            return " _ "


class Dealer(Hand):

    def dealer_rules(self):
        pass
