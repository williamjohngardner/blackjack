# BLACKJACK GAME by Bill Gardner

from hand import Hand
from functions import hit_stand

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


# start = input("Press Enter To Start")

player_card_1 = hand.deal(False)
player_card_2 = hand.deal(False)

player.append(player_card_1)
player.append(player_card_2)
print(player_card_1)
print(player_card_2)
print(player)

while len(player) < max_cards_in_hand:
    hit_stand()
    player.append(hit_stand)
    print(player)

