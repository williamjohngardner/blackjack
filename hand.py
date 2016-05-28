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


    def player_deal(self):

        player_card_1 = self.hand.deal_hand(True)
        player_card_2 = self.hand.deal_hand(True)

        self.player.append(player_card_1)
        self.player.append(player_card_2)

        return self.player

    '''
    def dealer_deal(self):
        dealer_card_1 = self.hand.deal_hand(True)  # Don't forget to change this to True when the game is complete
        dealer_card_2 = self.hand.deal_hand(False)

        self.dealer.append(dealer_card_1)
        self.dealer.append(dealer_card_2)

        return self.dealer
    '''

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

    def player_hand(self):

        while len(self.player) < self.max_cards_in_hand:
            choice = input("Would you like to Hit or Stand? H or S: ").lower()
            if choice == "h":
                new_card = self.hand.deal_hand(False)
                self.player.append(new_card)
                for card in self.player:
                    if card[0] in self.face_cards:
                        self.hand_value += 10
                    elif card[0] in self.number_cards:
                        self.hand_value += int(card[0])
                    elif card[0] == "A":  # This logic is not bullet proof.
                        self.hand_value += 11
                    elif self.player_start_value == 21:
                        print("\nYOU HIT 21!!!  YOU WIN!!!")
                        exit()

                if self.hand_value < 21:
                    continue
                elif self.hand_value == 21:
                    break
                elif self.hand_value > 21:
                    print("\nGAME OVER! YOU'VE BUSTED!")
                    exit()
            else:
                break
        return self.hand_value
