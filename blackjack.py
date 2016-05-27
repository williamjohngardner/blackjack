# BLACKJACK GAME by Bill Gardner

from deck_of_cards import DeckOfCards

print("*****************************" +
      "\n*****************************" +
      "\n**** AWESOME BLACKJACK!!!****"
      "\n*****************************" +
      "\n*****************************")

hand = DeckOfCards()
max_cards_in_hand = 5
player = []
dealer = []
face_cards = ["1", "J", "Q", "K"]
number_cards = "23456789"

# start = input("Press Enter To Start")

player_card_1 = hand.deal_hand(False)
player_card_2 = hand.deal_hand(False)
dealer_card_1 = hand.deal_hand(False)
dealer_card_2 = hand.deal_hand(False)

player.append(player_card_1)
player.append(player_card_2)
dealer.append(dealer_card_1)
dealer.append(dealer_card_2)

print(player_card_1)
print(player_card_2)
print("player" + str(player))

print("\n" + str(dealer_card_1))
print(dealer_card_2)
print("dealer" + str(dealer))

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
            elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
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
dealer_start_value = []
dealer_hand_value = []

for card in dealer:
    if card[0] in face_cards:
        dealer_start_value.append(10)
    elif card[0] in number_cards:
        dealer_start_value.append(int(card[0]))
    elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
        if sum(dealer_start_value) <= 10:
            dealer_start_value.append(11)
        else:
            dealer_start_value.append(1)
    else:
        dealer_start_value.append('#')

dealer_hand_value = sum(dealer_start_value)


while len(dealer) < max_cards_in_hand:
    if dealer_hand_value <= 17:
        new_card = hand.deal_hand(False)
        dealer.append(new_card)
        for card in dealer:
            if card[0] in face_cards:
                dealer_hand_value.append(10)
            elif card[0] in number_cards:
                dealer_hand_value.append(int(card[0]))
            elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
                if sum(dealer_hand_value) <= 10:
                    dealer_hand_value.append(11)
                else:
                    dealer_hand_value.append(1)
            else:
                dealer_hand_value.append('#')
        print(dealer)
        print(dealer_hand_value, str(sum(dealer_hand_value)))

        if sum(dealer_hand_value) <= 17:
            continue
        elif sum(dealer_hand_value) == 21:
            break
        elif sum(hand_value) > 21:
            print("\nDEALER BUSTED!!!  YOU WIN!!!")
            exit()
    else:
        break
