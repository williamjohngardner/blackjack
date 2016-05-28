# BLACKJACK GAME by Bill Gardner

# from deck_of_cards import DeckOfCards
from hand import Player


class BlackJack:

    print("*****************************" +
          "\n*****************************" +
          "\n**** AWESOME BLACKJACK!!!****"
          "\n*****************************" +
          "\n*****************************")

    # hand = DeckOfCards()
    max_cards_in_hand = 5
    player = []
    dealer = []
    face_cards = ["1", "J", "Q", "K"]
    number_cards = "23456789"
    ############# variables above will probably go away
    players = Player()

    # start = input("Press Enter To Start")
    player1 = players.player_deal()
    dealer1 = players.player_deal()
    player_start_value = players.start_value
    dealer_start_value = players.start_value

    print("Player's Hand", player1)
    print("Hand Value", players.start_value)
    print("\nDealer's Hand", dealer1)
    print("Hand Value", players.start_value)


    '''
    player_card_1 = hand.deal_hand(False)
    player_card_2 = hand.deal_hand(False)
    dealer_card_1 = hand.deal_hand(False)  # Don't forget to change this to True when the game is complete
    dealer_card_2 = hand.deal_hand(False)
    '''

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

    '''
    while len(player) < max_cards_in_hand:
        hand_value = 0
        choice = input("Would you like to Hit or Stand? H or S: ").lower()
        if choice == "h":
            new_card = hand.deal_hand(False)
            player.append(new_card)
            for card in player:
                if card[0] in face_cards:
                    hand_value += 10
                elif card[0] in number_cards:
                    hand_value += int(card[0])
                elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
                        hand_value += 11
                elif player_start_value == 21:
                    print("\nYOU HIT 21!!!  YOU WIN!!!")
                    exit()
            print(player)
            print(hand_value)

            if hand_value < 21:
                continue
            elif hand_value == 21:
                break
            elif hand_value > 21:
                print("\nGAME OVER! YOU'VE BUSTED!")
                exit()
        else:
            break
    '''
    players.player_hand()


    dealer_start_value = []

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
        elif sum(dealer_start_value) == 21:
            print("\nDEALER HIT 21!!!  DEALER WINS!!! GAME OVER!")
            exit()


    while len(dealer) < max_cards_in_hand:
        dealer_hand_value = 0
        if dealer_hand_value <= 17:
            new_card = hand.deal_hand(False)
            dealer.append(new_card)
            for card in dealer:
                if card[0] in face_cards:
                    dealer_hand_value += 10
                elif card[0] in number_cards:
                    dealer_hand_value += int(card[0])
                elif card[0] == "A":  # This logic is not yet bullet proof.  It needs to change based on the changing total.
                    dealer_hand_value += 11
                else:
                    dealer_hand_value.append('#')

            print(dealer, dealer_hand_value)

            if dealer_hand_value <= 17:
                continue
            elif dealer_hand_value == 21:
                break
            elif dealer_hand_value > 21:
                print("\nDEALER BUSTED!!!  YOU WIN!!!")
                exit()
