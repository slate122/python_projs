import random

# Card values: 2-10, face cards as 10, Aces as 11
val = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,
       7,7,7,7,8,8,8,8,9,9,9,9,
       10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
       11,11,11,11]  # Aces

# Card suits
suite = ['Spades','Hearts','Diamonds','Clubs']

# Generate card names like '2 of Spades', ..., 'A of Clubs'
cards = [str(x)+" of " + i for x in range(2,15) for i in suite]
cards = [card.replace('14', 'A').replace('11', 'J').replace('12', 'Q').replace('13', 'K') for card in cards]

# Map each card to its value
zip_cards = dict(zip(cards, val))

p = 0  # Play control flag

while p == 0:
    y = 0  # Round status flag
    random.shuffle(cards)
    
    print("Welcome to Blackjack!")
    print("Cards have been shuffled.")
    
    # Deal initial cards
    play = [cards[0], cards[2]]
    dealer = [cards[1], cards[3]]
    
    player_val = [zip_cards[card] for card in play]
    deal_val = [zip_cards[card] for card in dealer]
    
    # Handle case where two Aces = 22, which should display as 12
    print("Player's hand:", play, " ", '12' if sum(player_val) == 22 else sum(player_val))
    print("Dealer's hand:", dealer[0], " ", deal_val[0])

    if deal_val[0] == 11 and sum(deal_val) != 21:
        print("dealer does not have blackjack")
    
    # Check for blackjack conditions
    if (sum(deal_val) == 21) and sum(player_val) != 21:
        print("Dealer has blackjack!")
        y = 1
    elif sum(deal_val) != 21 and sum(player_val) == 21:
        print("Player has blackjack! Player wins!")
        y = 1
    elif sum(deal_val) == 21 and sum(player_val) == 21:
        print("Both player and dealer have blackjack! It's a tie!")
        y = 1
    else:
        # Player's turn
        while True and y == 0:
            # Adjust Ace from 11 to 1 if over 21
            if 11 in player_val and sum(player_val) > 21:
                index = player_val.index(11)
                player_val[index] = 1

            elif sum(player_val) == 21:
                print("BLACKJACK!")
                break

            elif input("Do you want to hit or stay? (h/s): ").lower() == 'h':
                # Deal new card
                play.append(cards[len(play) + len(dealer)])
                player_val.append(zip_cards[play[-1]])

                # Adjust all Aces as needed
                while 11 in player_val and sum(player_val) > 21:
                    index = player_val.index(11)
                    player_val[index] = 1

                print("Player's cards:", play, ' player total:', sum(player_val))
                print("Dealer's cards:", dealer[0])

                if sum(player_val) > 21:
                    print("Player busts! Dealer wins.")
                    y = 1
                    break
            else:
                print("You chose to stay.")
                break

        # Dealer's turn
        while True and y == 0:
            x = 'player total ' + str(sum(player_val)) + ' dealer total ' + str(sum(deal_val))

            # Adjust Ace if busting
            if 11 in deal_val and sum(deal_val) > 21:
                index = deal_val.index(11)
                deal_val[index] = 1

            elif sum(deal_val) < 17:
                print("Dealer hits.")
                dealer.append(cards[len(play) + len(dealer)])
                deal_val.append(zip_cards[dealer[-1]])
                print("Dealer's cards:", dealer)

            elif sum(deal_val) > 21:
                print(x)
                print("Dealer busts! Player wins.")
                break

            elif sum(deal_val) >= 17 and sum(deal_val) <= 21:
                print("Dealer stays.")
                if sum(deal_val) > sum(player_val):
                    print(x)
                    print("Dealer wins!")
                    break
                elif sum(deal_val) < sum(player_val):
                    print("Player wins!")
                    print(x)
                    break
                else:
                    print(x)
                    print("It's a tie!")
                    break

    # Ask if player wants another game
    if input("Do you want to play again? (y/n): ").lower() != 'y':
        p = 1
        print("Thanks for playing!")
    else: 
        print("Shuffling cards for the next game...")
        continue
