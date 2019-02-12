from graphics import *
from button import Button
from poker import Poker
from colordie import ColorDie

class Interface:
    def __init__(self):           
        self.win = win = GraphWin("Dice Poker", 400,400)
        win.setCoords(0,0,5.5,5.5)
        win.setBackground("lightblue")
        self.createDice()
        self.createDieButtons()
        self.buttons = []
        self.rollButton = Button(win, Point(2.75, 2.5), 4, 0.5, "Roll Dice")
        self.scoreButton = Button(win, Point(2.75, 1.5), 2, 0.5, "Score")
        self.quitButton = Button(win, Point(4.875, 0.25), 1, 0.25, "Quit")
        self.helpButton = Button(win, Point(0.625, 0.25), 1, 0.25, "Help")
        self.helpButton.activate()
        self.textBalance = Text(Point(2.75, 5), "$100").draw(win)
        self.textBalance.setStyle("bold")
        self.textBalance.setSize(20)
        self.textHand = Text(Point(2.75, 0.5), "Welcome to the Dice Table").draw(win)

        self.totatBalance = 0
        
    def createDice(self):
        self.dice = []
        center = Point(0.75, 4)
        for i in range(5):
            cdie = ColorDie(self.win, center, 0.75)
            self.dice.append(cdie)
            center.move(1,0)

    def createDieButtons(self):
        self.diceButtons = []
        centerButton = Point(0.75, 3.375)
        for i in range(5):
            dieNo = "Die " + str(i+1)
            dieButton = Button(self.win, centerButton, 0.75, 0.25, dieNo)
            #dieButton.activate()
            self.diceButtons.append(dieButton)
            centerButton.move(1,0)

    def showMoney(self, amt):
        self.textBalance.setText("$" + str(amt))

    def showDice(self, dice): #!!!!!
        # dice = [1,3,2,6,2] a random list of five elements with values 1-6
        i = 0
        for pos in dice:
            self.dice[i].setValue(pos)
            i += 1

    def playGame(self):
        self.rollButton.activate()
        self.quitButton.activate()
        while True:
            p = self.win.getMouse()
            if self.quitButton.clicked(p):
                # if quit then get user info
                # close the window
                # and return False to pokerapp to stop the game
                self.__savetoHighScoresTxt()
                self.win.close()
                return False
            elif self.rollButton.clicked(p):
                self.rollButton.deactivate()
                self.quitButton.deactivate()
                return True
            elif self.helpButton.clicked(p):
                self.__createHelpWindow()
                
    def __savetoHighScoresTxt(self):
        self.rollButton.deactivate()
        self.helpButton.deactivate()
        self.quitButton.setLabel("Done")
        Text(Point(2, 1), "Well Done!.  Type your username: ").draw(self.win)
        inputBox = Entry(Point(4, 1), 10).draw(self.win)
        self.win.getMouse()
        newName = inputBox.getText()
        inFile = open("highscores.txt", "r")
        names, balances = [], []
        for line in inFile:
            name, balance = line.split()
            names.append(name)
            balances.append(balance)
        if newName in names:
            for name in names:
                if newName == name:
                    if self.totalBalance > int(balances[names.index(name)]):
                        balances[names.index(name)] = self.totalBalance
        else:
            names.append(newName)
            balances.append(self.totalBalance)
        inFile.close()
        outFile = open("highscores.txt", "w")
        for i in range(len(names)):
            print(names[i], balances[i], file=outFile)
        outFile.close()
        
    def __createHelpWindow(self):
        win = GraphWin("Dice Poker Rules", 300,300)
        win.setCoords(0,0,10,10)
        payoffs = ["Two Pairs             $ 5",
                  "Three of a Kind       $ 8",
                  "Full House           $ 12",
                  "Four of a Kind       $ 15",
                  "Straight             $ 20",
                  "Five of a Kind       $ 30"]
        i = 0
        for line in payoffs:
            Text(Point(5, 8-i), line).draw(win)
            i += 1
        win.getMouse()
        win.close()

    def getInput(self):
        possitions = []
        self.rollButton.activate()
        self.scoreButton.activate()
        self.textHand.setText("...")
        for dieButton in self.diceButtons:
            dieButton.activate()
        p = self.win.getMouse()
        while not self.scoreButton.clicked(p):
            i = 0
            for die in self.dice:
                if self.diceButtons[i].clicked(p):
                    if i in possitions:
                        die.setColor("black")
                        possitions.remove(i)
                    elif i not in possitions:
                        die.setColor("grey")
                        possitions.append(i)
                i += 1
            possitions.sort()
            if self.rollButton.clicked(p):
                break
            if self.helpButton.clicked(p):
                self.__createHelpWindow()
            p = self.win.getMouse()
        self.rollButton.deactivate()
        self.scoreButton.deactivate()
        for dieButton in self.diceButtons:
            dieButton.deactivate()
        #reset the color back to original
        for die in self.dice:
            die.setColor("black")
        return possitions[:]
        
    def showResults(self, hand, castig, amt):
        self.totalBalance = amt
        self.showMoney(amt)
        self.textHand.setText(hand + "! You win $" + str(castig) + ".")

def __splashScreen():
        win = GraphWin("Dice Poker", 400,400)
        win.setCoords(0,0,5.5,5.5)
        win.setBackground("yellow")
        message = Text(Point(2.75, 4), "Welcome to Dice Poker").draw(win)
        message.setStyle("bold")
        message.setSize(20)
        description = Text(Point(2.75, 3), "Your initial balance will be $100.\nThere are 5 regular six-sided dice and you can roll them max 3 times.\nYou can also skip rolling if you already got a good hand\nand hit the score button instead.\nGood Luck !").draw(win)
        playButton = Button(win, Point(1.5, 2), 2, 0.5, "Let's Play!")
        playButton.activate()
        quitButton = Button(win, Point(4, 2), 2, 0.5, "Quit")
        quitButton.activate()
        while True:
            p = win.getMouse()
            if playButton.clicked(p):
                win.close()
                return True
            elif quitButton.clicked(p):
                win.close()
                return False
if __name__ == "__main__":
    if __splashScreen():       
        interface = Interface()
        app = Poker(interface)
        app.run()
