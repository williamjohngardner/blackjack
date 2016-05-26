from hand import Hand

def hit_stand():

    hand = Hand()
    hand.deal()

    h = ""
    s = ""

    choice = input("Would you like to Hit or Stand? H or S: ").lower()

    if choice == h:
        player_card = hand.deal(False)
        return player_card
    elif choice == s:
        pass  # This will move to the dealer's turn