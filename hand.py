from deck_of_cards import DeckOfCards


class Player:

    def __init__(self):
        self.hand = DeckOfCards()
        self.player = []
        self.dealer = []
        self.max_cards_in_hand = 5
        self.face_cards = ["1", "J", "Q", "K"]
        self.number_cards = "23456789"
        self.hand_value = 0
        self.start_value = 0

    def start_value(self):

        for card in self.player:
            if card[0] in self.face_cards:
                self.start_value += 10
            elif card[0] in self.number_cards:
                self.start_value += int(card[0])
            elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
                if self.start_value <= 10:
                    self.start_value += 11
                else:
                    self.start_value += 1
            elif self.start_value == 21:
                break
        return self.start_value


