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
player_hand = []
dealer = []
dealer_hand = []
face_cards = ["1", "J", "Q", "K"]
number_cards = ["2", "3", "4", "5", "6", "7", "8", "9"]


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
    choice = input("Would you like to Hit or Stand? H or S: ").lower()
    if choice == "h":
        player_card = hand.deal_hand(False)
        player.append(player_card)
        for card in player:
            if card[0] in face_cards:
                player_hand.append(10)
            elif card[0] in number_cards:
                player_hand.append(5)
            elif card[0] == "A":
                player_hand.append(11)  # or 1!!!
            else:
                player_hand.append(15)

        print(player)
        print(player_hand)
        continue
    else:
        break

'''
while len(dealer) < max_cards_in_hand:
    if sum(dealer) < 21:
        dealer_card = hand.deal_hand(False)
        dealer.append(dealer_card)
        print(dealer)
        continue
    else:
        break
'''