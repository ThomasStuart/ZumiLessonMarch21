from random import seed, randint


#  This function can be done with one for loop
#  Hint:  lists will be very useful .... suit = [...]  AJQK = [...]
def create_deck():
    deck = []  # create the list

    # create the diamonds cards 1-10 with a for loop  (amrutha)
    for index in range(1, 11):
        deck.append( ( "diamonds", str(index), index)  )

    deck.append(("diamonds", 'A', 1))
    deck.append(("diamonds", 'J', 11))
    deck.append(("diamonds", 'Q', 11))
    deck.append(("diamonds", 'K', 11))

    # create the spades cards 1-10 with a for loop  (johnavon)
    for index in range(1, 11):
        deck.append(("spades", str(index), index)  )

    deck.append(("spades", 'A', 1))
    deck.append(("spades", 'Q', 11))
    deck.append(("spades", 'K', 11))

    # create the clubs cards 1-10 with a for loop  (Jaeden)
    for index in range(1, 11):
        deck.append( ("clubs", str(index), index)  )

    deck.append(("clubs", 'A', 1))
    deck.append(("clubs", 'J', 11))
    deck.append(("clubs", 'Q', 11))
    deck.append(("clubs", 'K', 11))

    # create the hearts cards 1-10 with a for loop  (Bryan)
    for index in range(1, 11):
        deck.append(("hearts", str(index), index) )

    deck.append(("hearts", 'A', 1))
    deck.append(("hearts", 'J', 11))
    deck.append(("hearts", 'Q', 11))
    deck.append(("hearts", 'K', 11))
    return deck



def get_rand_card(deck, seed_num):
    seed(seed_num)
    index = randint(0, len(deck)-1)
    #delete the card from the deck
    card =  deck[index]
    del deck[index]

    return  deck, card

def get_dealer_hand(deck, seed_num):
    hand_sum = 0
    seed(seed_num)
    index = randint(0, len(deck)-1)

    cards_dealt = []

    while( True ):
        card = deck[index]
        del deck[index]

        if hand_sum + card[2] <= 21:
            hand_sum += card[2]
            cards_dealt += card
        else:
            break

    return  hand_sum, cards_dealt

# How do you call “create_deck” in one line?  And store it in ??
# set the list named “deck” equal to whatever “create_deck()” returns
deck = create_deck()
user_hand_count   = 0
dealer_hand_count = 0
does_want_another_card = True
user_cards = []

def print_deck(deck):
    for card in deck:
        print(card)



while( user_hand_count < 21 and does_want_another_card ):

    user_seed = input("Enter a random seed: ")
    user_seed = int(user_seed)

    deck, card = get_rand_card(deck, user_seed)
    user_cards += card

    print("You were dealt a", card[1], " of ", card[0])
    print()

    # increment your hand count based on the card dealt
    user_hand_count += card[2]

    # check if they won before asking for a new card
    if user_hand_count == 21:
        print( "You WON the game: " )
        break

    # ask the user if they want another card
    user_input = input("Want another card ( y for Yes, anything else for No)")
    if (user_input != 'y'):
        does_want_another_card = False


if user_hand_count != 21:

    dealer_seed = input("Enter a random seed: ")
    dealer_seed = int(dealer_seed)

    dealer_sum, dealer_cards = get_dealer_hand(deck,dealer_seed)


    print("    Your hand count is: ", user_hand_count)
    print(user_cards)
    print( "Dealers hand count is: ", dealer_sum)
    print(dealer_cards)
    

    if user_hand_count < dealer_sum:
        print("Dealer WON: ")
    else:
        print("You WON: ")



print("Program is over")
