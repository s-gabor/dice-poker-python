from random import randrange

class Dice:
    def __init__(self):
        self.dice = [0] * 5
        self.rollAll()
        
    def roll(self, possitions):
        for pos in possitions:
            self.dice[pos] = randrange(1,7)
            
    def rollAll(self):
        self.roll(range(5))
        
    def values(self):
        return self.dice[:]

    def score(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1
        if 5 in counts:
            hand, payout = "Five of a Kind", 30
        elif 4 in counts:
            hand, payout = "Four of a Kind", 15
        elif (2 in counts) and (3 in counts):
            hand, payout = "Full House", 12
        elif 3 in counts:
            hand, payout = "Three of a Kind", 8
        elif not 2 in counts and (counts[1] == 0 or counts[6] == 0):
            hand, payout = "Straight", 15
        elif counts.count(2) == 2:
            hand, payout = "Two Pairs", 5
        else:
            hand, payout = "Garbage", 0
        return hand, payout
