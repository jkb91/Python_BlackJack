import random

win_count = 0
hand_value = 0
bet = 0
wallet = 1000
game = True
turn = 'Player'

class Deck(object): #class containing deck and shuffle
    deck = ['2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds',
            '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds',
            '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds',
            'A of Diamonds', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades',
            '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades',
            '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades',
            'A of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts',
            '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts',
            '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts',
            'A of Hearts', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs',
            '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs',
            '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs',
            'A of Clubs']
    
    random.shuffle(deck)
    new_deck = ['2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds',
            '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds',
            '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds',
            'A of Diamonds', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades',
            '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades',
            '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades',
            'A of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts',
            '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts',
            '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts',
            'A of Hearts', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs',
            '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs',
            '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs',
            'A of Clubs']
    
    def reset_deck(): # restock/reshuffle deck after game
        global d_hand, hand
        random.shuffle(Deck.deck)
        hand = [] #emptying hand
        d_hand = []
        hand = [Deck.deck[1], Deck.deck[3]] # populating hand
        d_hand = [Deck.deck[0], Deck.deck[2]]

        ### use as reference deck to restock deck when restarting

class Game(Deck): # class containing hit and stay as well as calculating the value, uses Deck class as object
    global hand, d_hand, turn, hand_value, bet, wallet

    def value(val_hand): # calculates value
        hand_value = 0
        if val_hand == 'Player':
            for i in range(0, len(hand)): # convert cards into numbers based on first character 
                if hand[i][0] == 'J' or hand[i][0] == 'Q' or hand[i][0] == 'K':
                    hand_value += 10
                elif hand[i][0] == 'A': 
                    hand_value += 11
                elif hand[i][:2] == '10':
                    hand_value += 10
                else:
                    hand_value += int(hand[i][0])
            if hand_value > 21:  # when calculating value, if its a bust, change Ace value to 1
                for i in range(0, len(hand)):
                    if hand[i][0] == 'A':
                        hand_value -= 10
            return(hand_value)
        elif val_hand == 'Dealer':
            for i in range(0, len(d_hand)): # convert cards into numbers based on first character 
                if d_hand[i][0] == 'J' or d_hand[i][0] == 'Q' or d_hand[i][0] == 'K':
                    hand_value += 10
                elif d_hand[i][0] == 'A': 
                    hand_value += 11
                elif d_hand[i][:2] == '10':
                    hand_value += 10
                else:
                    hand_value += int(d_hand[i][0])
            if hand_value > 21:  # when calculating value, if its a bust, change Ace value to 1
                for i in range(0, len(d_hand)):
                    if d_hand[i][0] == 'A':
                        hand_value -= 10
            return(hand_value)
        
    

    def bust_check(bust, hand_value):  # returns values if bust or blackjack
        if bust == 'Player' and hand_value > 21:
            return "player bust"
        elif bust == 'Player' and hand_value == 21:
            return "player blackjack"
        elif bust == 'Dealer' and hand_value > 21:
            return "dealer bust"
        elif bust == 'Dealer' and hand_value == 21:
            return "dealer blackjack"
            

    def hit(hit_hand):  # appends a card and then removes it from pool of available cards
        if hit_hand == 'Player':
            hand.append(Deck.deck[0])
            del Deck.deck[0]
            Game.bust_check('Player', Game.value('Player'))
            if Game.bust_check('Player', Game.value('Player')) == 'player bust':  # if bust or black jack, shows hand and ends game
                print("Player busts!")
                print(hand)
                Game.call(0,1)
            elif Game.bust_check('Player', Game.value('Player')) == 'player blackjack':
                print("Player hits blackjack!")
                Game.call(1,0)
            
        elif hit_hand == 'Dealer':
            print("Dealer hits!")
            d_hand.append(Deck.deck[0])
            del Deck.deck[0]
            print("You see the dealer has {0} and a facedown card".format(d_hand[1:]))
            if Game.bust_check('Dealer', Game.value('Dealer')) == 'dealer bust':
                print("Dealer busts with {0}".format(Game.value('Dealer')))
                print("Dealer's hand: {0}".format(d_hand))
                Game.call(1,0)
            elif Game.bust_check('Dealer', Game.value('Dealer')) == 'dealer blackjack':
                print("Dealer hits blackjack!")
                Game.call(0,1)

    def stay(stay_hand):    # function if player chooses to stand or dealer gets above 16
        if stay_hand == 'Player':
            print("You've chosen to stay at {0}".format(Game.value('Player')))
        elif stay_hand == 'Dealer':
            Game.call(Game.value('Player'), Game.value('Dealer'))

    
    def call(player_final_value, dealer_final_value):  # End of game calculation of winner and loser
        global wallet, turn, win_count
        if player_final_value != 1 and player_final_value != 0:
            print("Dealer's hand: {0}".format(d_hand))
            print("Player has {0}, Dealer has {1}".format(player_final_value, dealer_final_value))
        if player_final_value > dealer_final_value:  # if win add bet if loss subtract bet
            print("You win!!!")
            wallet += bet
            print("Your bet was {0}, you now have a total of {1} dollars in your wallet!!!".format(bet, wallet))
            win_count += 1
        elif dealer_final_value > player_final_value:
            print("You lose...")
            wallet -= bet
            print("Your bet was {0}, you now have a total of {1} dollars left in your wallet!!!".format(bet, wallet))
            win_count -= 1
        if player_final_value == dealer_final_value:
            print(" It's a push!!")
            print("You still have {0} dollars left in your wallet.".format(wallet))
            
        turn = 'restart'

Deck()
Game()              
                
hand = [Deck.deck[1], Deck.deck[3]] # populating hand
d_hand = [Deck.deck[0], Deck.deck[2]]


print("Welcome to Python BlackJack!")
print("You currently have {0} dollars".format(wallet))
bet = int(input("How much would you like to bet? (numbers only): "))
if bet >= wallet:
                print("GOING ALL IN!!")
                bet = wallet
                      
del Deck.deck[0:4] #deletes first four cards given to player and dealer from pool of available cards
while game == True: 
    if turn == 'Player':
        print("Your hand: {0}".format(hand))
        Game.bust_check('Dealer', Game.value('Dealer'))
        print("You see the dealer has {0} and a facedown card".format(d_hand[1:]))
        move = input("Do you want to hit or stand?: ")
        if move[:3].upper() == 'HIT':
            Game.hit('Player')
        if move[:3].upper() == 'STA': 
            Game.stay('Player')
            turn = 'Dealer'
    elif turn == 'Dealer':
        if Game.value('Dealer') <= 16:
            Game.hit('Dealer')
        else:    
            Game.stay('Dealer')
            turn = 'restart'
    elif turn == 'restart':
        print("You're up {0} game(s)".format(win_count))
        play_again = input("Do you want to play again ? (Y\\N): ")
        if play_again[0].upper() != 'N':
            if wallet <= 0:
                print("You're out of money!!, Resetting bank to 1000......")
                wallet = 1000
            bet = int(input("How much would you like to bet? (numbers only): "))
            if bet >= wallet:
                print("GOING ALL IN!!")
                bet = wallet
            Deck.deck = Deck.new_deck
            Deck.reset_deck()
            turn = 'Player'
        else:
            break
       


