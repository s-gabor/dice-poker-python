from poker import Poker

class Interface:
    def __init__(self):
        print("\nDICE POKER\n")
        print("Your initial balance is $100.")
        print("You can roll 3 times and each one costs $10.")

    def showMoney(self, amt):
        print("Your current balance is: $" + str(amt))

    def showDice(self, dice):
        print("You have:", dice)

    def playGame(self):
        choice = input("Would you like to try your luck? ")
        if choice[0] in "yY":
            return True
        else:
            return False
    
    def getInput(self):
        return eval(input("Select the dice you want to roll([] to check): "))
        
    def showResults(self, hand, win, amt):
        print(hand + ". You won $" + str(win))
        print("You currently have $" + str(amt) + ".")

if __name__ == "__main__":
    interface = Interface()
    app = Poker(interface)
    app.run()
