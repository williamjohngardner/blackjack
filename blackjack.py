# BLACKJACK GAME by Bill Gardner

from hand import Hand

print("*****************************" +
      "\n*****************************" +
      "\n**** AWESOME BLACKJACK!!!****"
      "\n*****************************" +
      "\n*****************************")

hand = Hand()

num_cards_dealt = 2
max_cards_in_hand = 5
player = []
dealer = []
h = ""
s = ""


# start = input("Press Enter To Start")

player_card_1 = hand.deal(False)
player_card_2 = hand.deal(False)

player.append(player_card_1)
player.append(player_card_2)
print(player_card_1)
print(player_card_2)
print(player)

while len(player) < max_cards_in_hand:
    choice = input("Would you like to Hit or Stand? H or S: ").lower()
    if choice == h:
        player_card = hand.deal(False)
        player.append(player_card)
        print(player)
        continue
    else:
        # This will move to the dealer's turn
        break





