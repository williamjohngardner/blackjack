# BLACKJACK GAME by Bill Gardner

from deck_of_cards import DeckOfCards


class BlackJack:

    def __init__(self):
        hand = DeckOfCards()
        max_cards_in_hand = 5
        player = []
        dealer = []
        face_cards = ["1", "J", "Q", "K"]
        number_cards = "23456789"
        hand_value = 0

        print("*****************************" +
              "\n*****************************" +
              "\n**** AWESOME BLACKJACK!!!****"
              "\n*****************************" +
              "\n*****************************")

        # start = input("Press Enter To Start")

        player_card_1 = hand.deal_hand(True)
        player_card_2 = hand.deal_hand(True)
        dealer_card_1 = hand.deal_hand(True)  # Don't forget to change this to False when the game is complete
        dealer_card_2 = hand.deal_hand(True)

        player.append(player_card_1)
        player.append(player_card_2)
        dealer.append(dealer_card_1)
        dealer.append(dealer_card_2)

        print("Player Hand: ", player)
        print("Dealer Hand: ", dealer)
        '''
        player_start_value = []

        for card in player:
            if card[0] in face_cards:
                player_start_value.append(10)
            elif card[0] in number_cards:
                player_start_value.append(int(card[0]))
            elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
                if sum(player_start_value) <= 10:
                    player_start_value.append(11)
                else:
                    player_start_value.append(1)
            elif sum(player_start_value) == 21:
                print("\nYOU HIT 21!!!  YOU WIN!!!")
                exit()
        '''
        while len(player) < max_cards_in_hand:
            hand_value = 0
            choice = input("Would you like to Hit or Stand? H or S: ").lower()
            if choice == "h":
                new_card = hand.deal_hand(True)
                player.append(new_card)
                for card in player:
                    if card[0] in face_cards:
                        hand_value += 10
                    elif card[0] in number_cards:
                        hand_value += int(card[0])
                    elif card[0] == "A" and hand_value > 11:
                        hand_value += 1
                    elif card[0] == "A" and hand_value < 11:
                        hand_value += 10
                print(player)
                print(hand_value)

                if hand_value < 21:
                    continue
                elif hand_value == 21:
                    break
                elif hand_value > 21:
                    break
            else:
                break

        dealer_start_value = 0

        for card in dealer:
            if card[0] in face_cards:
                dealer_start_value +=10
            elif card[0] in number_cards:
                dealer_start_value += int(card[0])
            elif card[0] == "A":
                if dealer_start_value <= 10:
                    dealer_start_value += 11
                else:
                    dealer_start_value += 1
            elif dealer_start_value == 21:
                break

        dealer_hand_value = dealer_start_value

        while len(dealer) < max_cards_in_hand:
            if 21 >= dealer_hand_value >= 17:
                break
            elif dealer_hand_value < 17:
                new_card = hand.deal_hand(True)
                dealer.append(new_card)
                for card in dealer:
                    if card[0] in face_cards:
                        dealer_hand_value += 10
                    elif card[0] in number_cards:
                        dealer_hand_value += int(card[0])
                    elif card[0] == "A" and dealer_hand_value > 11:
                        dealer_hand_value += 1
                    elif card[0] == "A" and dealer_hand_value < 11:
                        dealer_hand_value += 10
                print(dealer, dealer_hand_value)
            elif dealer_hand_value > 21:
                break
            else:
                break

        if dealer_hand_value > 21:
            print("You Win! Dealer Busted!")
            exit()
        elif hand_value > 21:
            print("You've Busted! Game Over!")
        elif player == 21:
            if player == dealer:
                print("Tie! Dealer Wins!")
                exit()
            else:
                print("BlackJack!  You Win!")
                exit()
        elif player > dealer:
            print("Player wins!")
            exit()
        elif dealer < player:
            print("Dealer wins!")
            exit()
        elif player == dealer:
            print("Tie! Dealer wins!")
            exit()

blackjack = BlackJack()