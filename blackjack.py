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
print(player)

print(dealer_card_1)
print(dealer_card_2)
print(dealer)

while len(player) < max_cards_in_hand:
    choice = input("Would you like to Hit or Stand? H or S: ").lower()
    if choice == "h":
        player_card = hand.deal_hand(False)
        player.append(player_card)
        print(player)
        continue
    else:
        break

while len(dealer) < max_cards_in_hand:
    if sum(dealer) <= 21:
        dealer_card = hand.deal_hand(False)
        dealer.append(dealer_card)
        print(dealer)
        continue
    else:
        break
