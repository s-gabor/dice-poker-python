from dice import Dice

class Poker:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.playGame():
            self.dice.rollAll()
            self.playRound()
            
    def playRound(self):
        rolls = 1
        self.money = self.money - 10
        self.interface.showMoney(self.money)
        while rolls < 3:
            self.interface.showDice(self.dice.values())
            possitions = self.interface.getInput()
            if possitions == []:
                break
            self.dice.roll(possitions)
            rolls += 1
        self.interface.showDice(self.dice.values())
        hand, payout = self.dice.score()
        self.money = self.money + payout
        self.interface.showResults(hand, payout, self.money)
