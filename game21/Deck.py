__author__ = "Adrian Szatmari"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adrian Szatmari"
__status__ = "Production"

import random
import math

class Deck:
    """
    This class implements a deck, with the main argument being the number of players. 
    A single card is just an integer, representing the position in the array representing a deck.
    There needs to be one deck per 3 players. 
    The important method here is drawCard(), that randomly picks a card from the remaining deck.
    """
    def __init__(self, nb_players):
        #one deck per 3 players
        nb_decks = math.ceil(nb_players/3)
        a_deck = [4,4,4,4,4,4,4,4,4,4,4,4,4]
        #count the aces in position 0
        self.nb_cards = nb_decks*13*4
        self.cards = [x * nb_decks for x in a_deck]

    def drawCard(self):
        """
        This function picks a card from the deck in a random order, then updates the deck.
        """
        if(self.nb_cards< 1):
            return -1
        else:
            #lay out all the cards, and pick one
            c = random.randrange(0,self.nb_cards)
            for index, x in enumerate(self.cards):
                c -= x
                if(c < 0):
                    #shave of card types until you get to the right card equiv. class
                    c = index
                    break
            self.cards[c] -= 1
            self.nb_cards -= 1
            #a card is just an integer here, representing the position in self.cards
            return c

    def toString(self):
        """
        This function returns a string that prints the current state of the deck.
        """
        string = ""
        lengths1 = [3,3,3,3,3,3,3,3,3,3,4,5,4]
        names = "Cards: \t | Ace | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | Jack | Queen | King |"
        lengths2 = [len(str(x)) for x in self.cards]
        diff_length = [a_i - b_i for a_i, b_i in zip(lengths1, lengths2)]
    
        vals = "Number:\t | "
        for i in range(len(self.cards)):
            vals += str(self.cards[i])
            vals += " "*diff_length[i]
            vals += " | "
    
        string += names
        string += "\n"
        string += vals
        return string

