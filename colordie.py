from die import Die

class ColorDie(Die):
    def setValue(self, value):
        self.value = value         #stores the value for use in setColor
        Die.setValue(self, value)  #is accessing the method setValue from Die

    def setColor(self, color):
        self.foreground = color   #sets the user input color pips(from Die class)
        self.setValue(self.value)  #is acessing the method setValue(from ColorDie)
    
