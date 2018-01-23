__author__ = "Adrian Szatmari"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adrian Szatmari"
__status__ = "Production"

class Hand:
    """
    This class implements the a hand, i.e. a set of cards of a player belongin together.
    A hand has a list of cards, a last card added, a bet. 
    Moreover, a hand has a list of scores associated, since an Ace can have value 1 or 11.  
    The most important function is addCard(), adding a card to the hand and updating the scores. 
    """
    values = [1,2,3,4,5,6,7,8,9,10,1,2,3,11]

    def __init__(self):
        self.last_card = -1 #index of the last card, no cards yet
        self.cards = [0,0,0,0,0,0,0,0,0,0,0,0,0] #the actual hand
        self.scores = [0] #in case of one or multiple Aces
        self.bet = 0
    
    def setBet(self, bet):
        self.bet = bet

    def bestScore(self):
        """
        This function returns the score closest to 21, but under it. 
        In case the hand has no card or if all the scores are above 21,
        the function return -1.
        """
        #restrict to the scores under 21
        temp_scores = [i for i in self.scores if i <= 21]
        if(len(temp_scores) == 0): #if the hand is empty or all scores are above 21
            return -1
        else: 
            return max(temp_scores) 

    def addCard(self,card):
        """
        This function adds a card to the current hand. In particular, it updates the scores
        correctly. One has to be careful because Aces are worth 1 or 11, and one should not 
        decided a priori. 
        """
        self.last_card = card 
        self.cards[card] += 1 #actually put the card into the hand
        if(self.last_card != 0): #not an ace
            val = Hand.values[self.last_card]
            self.scores = [x + val for x in self.scores]
        else: #last card is an ace
            temp1 = self.scores
            temp2 = self.scores 
            temp1 = [x + Hand.values[0] for x in temp1] #if ace is worth 1
            temp2 = [x + Hand.values[-1] for x in temp2] #if ace is worth 11
            #restrict to the unique set of possible scores
            self.scores = list(set().union(temp1,temp2)) 

    def toString(self):
        """
        This function returns a string that prints the current state of the hand.
        """
        names = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        string = "[Scores:"
        for i in self.scores:
            string += str(i)
            string += ","
        string = string[:-1]
        
        string += "|Bet:"
        string += str(self.bet)
        string += "|"

        string += "Cards:"
        for index, i in enumerate(self.cards):
            if(i > 0):
                for x in range(i):
                    string += names[index]
                    string += ","
        string = string[:-1]
        string += "]"
        return string