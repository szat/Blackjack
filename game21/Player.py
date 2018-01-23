__author__ = "Adrian Szatmari"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adrian Szatmari"
__status__ = "Production"

import Hand

class Player:
    """
    This class implements a player, i.e. an agent that has a set of hands and some possible actions.
    There are 3 important actions that a player can take, thus deciding into which state it will transition. 
    Namely, thinkHit(deck_array), thinkSplit(new_card), and splitHand(new_card).
    The player is always acting with respect to the current hand, indexed by current_hand_index.
    Thus when thinkHit(deck_array) is invoked, the player estimate whether to hit, with respect to the current hand. 
    Similarly to thinkSplit and splitHand, and the other methods, are w.r.t. to the current hand.
    
    thinkHit(...) estimates the probability the score with remain under 21 when the next card is drawn.
    thinkSplit(...) codes expert knowledge about when to split a hand, if it is possible at all. 
    splitHand(...) splits the current hand into the current hand and the next hand. 
    """
    values = [1,2,3,4,5,6,7,8,9,10,1,2,3,11]
    
    def __init__(self):
        #a player starts with one hand
        h = Hand.Hand()
        self.current_hand_idx = 0
        self.hands = [h]
    
    def addCard(self, card):
        #this function uses the addCard function from the class Hand
        self.hands[self.current_hand_idx].addCard(card)
    
    def thinkHit(self,deck_array):
        """
        This function takes in the current state of the deck, as represented by an array.
        It then output the probability that the next card's value will be under (21 - best score)
        In this way, it is possible to control the risk taking factor of the player through probabilities. 
        """
        cards_remaining = sum(deck_array)
        #there are no more cards in the deck 
        if(cards_remaining < 1):
            return 0
        else:
            #find the most lenient score
            scores = self.hands[self.current_hand_idx].scores
            diff = [21 - x for x in scores]
            diff = max(diff)
            if diff < 1:
                return 0
            else:
                #count the number of cards whose value is under diff
                cummulative = 0
                last_card = self.hands[self.current_hand_idx].last_card
                for index, x in enumerate(deck_array):
                    if(Player.values[index] < diff or index == last_card):
                        cummulative += x
                #this is the frequential probability of getting a good card
                return cummulative / cards_remaining
    
    def thinkSplit(self, new_card):
        """
        This function takes in a card, i.e. an integer representing an index in the deck_array.
        If this new card is the same as the last drawn card, then it is possible to split the hands. 
        This function returns 0 if it thinks that the hand should not be split. 
        This function returns 1 if it thinks that the hand should be split. 
        These decisions are taken from expert knowledge that is available in the literature on 21. 
        """
        current_hand = self.hands[self.current_hand_idx]
        last_card = current_hand.last_card
        if(last_card != new_card):
            return 0
        else:
            temp = current_hand
            temp.addCard(new_card)
            min_score = min(temp.scores)
            if(min_score > 21):
                return 1
            elif(new_card == 1):
                return 1
            elif(min_score > 19):
                return 0
            elif(new_card == 8):
                return 1
            else: 
                return 0

    def splitHand(self, new_card, bet):
        #add a new hand to the player, but the do not change the current hand
        new_hand = Hand.Hand()
        new_hand.addCard(new_card)
        self.hands.insert(self.current_hand_idx+1, new_hand)
        self.hands[self.current_hand_idx+1].setBet(bet)
        
    def lastCard(self):
        return self.hands[self.current_hand_idx].last_card
    
    def minScore(self):
        return min(self.hands[self.current_hand_idx].scores)

    def currentBet(self):
        return self.hands[self.current_hand_idx].bet

    def toString(self):
        """
        This function returns a string that prints the current state of the hand.
        """
        string = ""
        for i in self.hands:
            string += i.toString()
            string += "  "
        string = string[:-1]
        return string