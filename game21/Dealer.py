__author__ = "Adrian Szatmari"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adrian Szatmari"
__status__ = "Production"

import Hand

class Dealer: 
    """
    This class implements a dealer, i.e. an agent that has a set of hands and some possible actions.
    There is 1 important action that a dealer can take, thus deciding into which state it will transition. 
    Namely, thinkHit(deck_array): the dealer when thinkHit(deck_array) is invoked, the dealer estimates whether to hit or to stand.
    The deterministic rules are implemented. Namely, if the total score is less than or equal to 16 then hit, otherwise stand. 
    """

    def __init__(self):
        h = Hand.Hand()
        self.hand = h

    def addCard(self, card):
        #this function adds a card to the dealer, using the addCard() function from class Hand
        self.hand.addCard(card)
    
    def thinkHit(self):
        """
        This function return 1 if the dealer is supposed to get a new card, and 0 otherwise. 
        When the score of the dealer's hand is less than or equal to 16, get a new card, so return 1. 
        Otherwise return 0.
        """
        hand_val = min(self.hand.scores)
        if(hand_val <= 16):
            return 1
        else:
            return 0

    def toString(self):
        """
        This function returns a string that prints the current state of the hand.
        """
        return self.hand.toString()