from deck_of_cards import DeckOfCards


class Player:

    def __init__(self):
        self.card = DeckOfCards()
        self.card.deal_hand()


    def player(self):

        while len(player) < max_cards_in_hand:
            hand_value = []
            choice = input("Would you like to Hit or Stand? H or S: ").lower()
            if choice == "h":
                new_card = hand.deal_hand(False)
                player.append(new_card)
                for card in player:
                    if card[0] in face_cards:
                        hand_value.append(10)
                    elif card[0] in number_cards:
                        hand_value.append(int(card[0]))
                    elif card[
                        0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
                        if sum(hand_value) <= 10:
                            hand_value.append(11)
                        else:
                            hand_value.append(1)
                    else:
                        hand_value.append('#')
                print(player)
                print(hand_value, str(sum(hand_value)))

                if sum(hand_value) < 21:
                    continue
                elif sum(hand_value) == 21:
                    break
                elif sum(hand_value) > 21:
                    print("\nGAME OVER! YOU'VE BUSTED!")
                    exit()
            else:
                break


class Dealer(Player):

    def dealer_rules(self):
        pass
