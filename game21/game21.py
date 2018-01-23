__author__ = "Adrian Szatmari"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adrian Szatmari"
__status__ = "Production"

import math, random
import Deck, Player, Dealer

card_names = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"] 

def inputNbPlayers():
    """
    This function is a while loop to catch the number of players from the command line. 
    Verifies whether the input is a positive integer, otherwise asks again.
    """
    while True:
        try:
            nb_players = int(input("Please enter the number of players: "))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if(nb_players < 1):
                print("Integer must be bigger than 1! Try again.")
                continue
            break 
    return nb_players

def inputBet():
    """
    This function is a while loop to catch the number bet of a player from the command line.
    Verifies whether the input is a positive integer, otherwise asks again.
    """
    while True:
        try:
            bet_amount = int(input("Please enter your initial bet: "))       
        except ValueError:
            print("Bet has to be an integer! Try again.")
            continue
        else:
            if(bet_amount <= 0):
                print("Bet must be positive! Try again.")
                continue
            break 
    return bet_amount

def inputLoop(inputList):
    """
    This is a simple function that takes as input a list of strings.
    The function is a while loop to catch one of the terms of the list from the command line. 
    Verifies whether the input is in the input list, otherwise asks again. 
    """
    string = ""
    string += "Please choose one input from ["
    for i in inputList:
        string += i
        string += ","
    string = string[:-1]
    string += "]: "
    inputString = ""
    while True:
        inputString = input(string)
        if(inputString in inputList):
            return inputString
        else:
            continue

### PROGRAM START ###

print("Welcome to this game of 21!")
print("The rules of 21 are the following: ")
print("\t-1: \tFirst place a bet, each player at the table places a bet;")
print("\t-2: \tThe dealer will give itself first, then to all the players, a card from the deck;")
print("\t\tThese cards are facing up, so that everyone can see them;")
print("\t-3: \tEach player plays: as one player finishes playing, it will not play again;")
print("\t\tThe goal is to get as close as possible to the score of 21;")
print("\t\tThe value of the cards are: 1 or 11 for the aces, 1 for jacks, 2 for queens, 3 for kings;")
print("\t\tFor the rest of the cards, the values correspond to their number, i.e. 3 has value 3;")
print()
print("\t\tA player's current hand is \"bust\" when the score of the hand is above 21;") 
print("\t\tIn that case the hand will automatically lose;")
print("\t\tA player can ask to \"hit\", i.e. get a new card, if the hand is still under 21;") 
print("\t\tA player can ask to \"stand\" to pass the current hand, but a player can have more than one hand;")
print("\t\tA player can ask to \"split\" if the new card is the same as the previous card (no suit);")
print("\t\tIn that case a new hand is created with the new card, with the same betting value as the previous hand;")
print("\t\tThe next time the player asks to \"hit\", it is for the previous hand;")
print()
print("\t-4: \tWhen all the players are done, i.e. when they are bust or they \"stand\":")
print("\t\t\tThe dealer will draw a new card if its score is under 16;")
print("\t\t\tThe dealer will stop drawing cards if its score is above 17;")
print("\t-5: \tThe players that are bust automatically lose.")
print("\t\tOf the players that are not bust, if the dealer is bust, everyone wins;")
print("\t\tOf the players that are not bust, if the dealer is not bust:")
print("\t\tthe ones with scores higher or equal to the dealer's score win.")
print()

#initialization
#get number of players
nb_players = inputNbPlayers()
deck = Deck.Deck(nb_players)
dealer = Dealer.Dealer()
players = [Player.Player() for i in range(nb_players)]
human_idx = random.randrange(0,nb_players)

print("You are in position ", human_idx, " (starting from 0)!")

#getting the bets 
print("Everyone places a bet:")
for i in range(human_idx):
    bet_amount = random.randrange(1,99)
    players[i].hands[0].setBet(bet_amount)
    print("Player #",str(i),"'s bet is: \t",str(bet_amount))

#getting your bet
bet_amount = inputBet()
players[human_idx].hands[0].setBet(bet_amount)
print("Your bet is: \t\t", players[human_idx].hands[0].bet)

#getting the bets
for i in range(human_idx+1,nb_players):
    bet_amount = random.randrange(1,99)
    players[i].hands[0].setBet(bet_amount)
    print("Player #",str(i),"'s bet is: \t",str(bet_amount))

print()
print("Everyone gets a first card, face up:")

#getting the first cards
dealer.addCard(deck.drawCard())
print("Dealer: \t",dealer.toString())

#getting the first cards
for i in range(human_idx):
    players[i].addCard(deck.drawCard())
    print("Player #"+str(i)+":\t"+players[i].toString())

#getting your first cards
players[human_idx].addCard(deck.drawCard())
print("Your game:\t"+players[i].toString())

#getting the first cards
for i in range(human_idx+1,nb_players):
    players[i].addCard(deck.drawCard())
    print("Player #"+str(i)+":\t"+players[i].toString())

#computer plays
#note that you can adjust the risk taking with thinkHit(deck.card) > p
#where, p is a probability, so p = 0.4 would be more risky
print()
print("Everyone plays in a round-robin fashion:")
#computer players
for i in range(human_idx):
    while(players[i].current_hand_idx != len(players[i].hands)):
        if(players[i].thinkHit(deck.cards) > 0.5):
            card = deck.drawCard()
            if(players[i].thinkSplit(card) > 0.5):
                #make it simple
                bet = players[i].currentBet()
                players[i].splitHand(card, bet)
            else:
                players[i].addCard(card)
        else:            
            players[i].current_hand_idx += 1
#display the computer players
for i in range(human_idx):
    print("Player #" + str(i) + ":\t" + players[i].toString())

#human player
print()
print("It is your turn. Here is the state of the deck:")
print(deck.toString())
print()
#go through all the hands
while(players[human_idx].current_hand_idx < len(players[human_idx].hands)):
    if(players[human_idx].minScore() >= 21):
        players[human_idx].current_hand_idx += 1
    else:
        print("Your play: " + players[human_idx].toString())
        toDo = inputLoop(["hit","stand"])
        if(toDo == "hit"):
            card = deck.drawCard()
            if(card == players[human_idx].lastCard()):
                print("You can split your play, the new card is: " + card_names[card])
                toSplit = inputLoop(["split","pass"])
                if(toSplit == "split"):
                    bet = players[human_idx].currentBet()
                    players[human_idx].splitHand(card, bet)
                else:
                    players[human_idx].addCard(card)
            else:
                players[human_idx].addCard(card)
        else: #go to the next hand
            players[human_idx].current_hand_idx += 1
#display hand
print("Your play: " + players[human_idx].toString())
print()

#computer players
for i in range(human_idx+1,nb_players):
    while(players[i].current_hand_idx != len(players[i].hands)):
        if(players[i].thinkHit(deck.cards) > 0.5):
            card = deck.drawCard()
            if(players[i].thinkSplit(card) > 0.5):
                bet = players[i].currentBet()
                players[i].splitHand(card, bet)
            else:
                players[i].addCard(card)
        else:            
            players[i].current_hand_idx += 1
#display the rest of the computer players
for i in range(human_idx+1,nb_players):
    print("Player #" + str(i) + ":\t" + players[i].toString())

#let the dealer play
print()
print("The dealer is playing:")

#dealer playing
while(dealer.thinkHit() > 0.5):
    card = deck.drawCard()
    dealer.addCard(card)
print("Dealer: \t" + dealer.toString())

#resolution of who won and who lost
print()
print("Winners (W) and losers (L):")

dealer_score = dealer.hand.bestScore()
player_scores = []
for index, pl in enumerate(players):
    player_scores.append([])
    for j in pl.hands:
        player_scores[index].append(j.bestScore())

print()
if(dealer_score == -1):
    print("Dealer's score: bust")
else:
    print("Dealer's score: ", dealer_score)
for index, sublist in enumerate(player_scores):
    if(index == human_idx):
        string = "Your hand(s):\t\t"
    else:
        string = "Player #" + str(index) + "'s hand(s):\t"
    for ind2, s in enumerate(sublist):
        if(s == -1):
            string += " hand id:" + str(ind2) + ", score: bust => \tL;"
        else:
            if(s < dealer_score):
                string += " hand id:" + str(ind2) + ", score: " + str(s) + " => \tL;"
            else:
                string += " hand id:" + str(ind2) + ", score: " + str(s) + " => \tW;"
    print(string)

#finishing the program
print()
print("Thanks you for having played this little game of 21!")
print("Created by Adrian Szatmari.")
print("The game will now exit.")