from graphics import *
from button import Button
from random import randrange

class Die:
    def __init__(self, win, center, side):
        self.win = win
        self.center = center
        self.pipsize = side / 10
        hsize = side/2
        offset = side/4
        self.background = "white"
        self.foreground = "black"
        self.value = 1
        x, y = center.getX(), center.getY()
        p1 = Point(x - hsize, y - hsize)
        p2 = Point(x + hsize, y + hsize)
        face = Rectangle(p1, p2)
        face.draw(win)
        face.setFill(self.background)

        self.pips = [self.__makePip(Point(x-offset, y-offset), self.pipsize),
                     self.__makePip(Point(x-offset, y), self.pipsize),
                     self.__makePip(Point(x-offset, y+offset), self.pipsize),
                     self.__makePip(Point(x, y), self.pipsize),
                     self.__makePip(Point(x+offset, y-offset), self.pipsize),
                     self.__makePip(Point(x+offset, y), self.pipsize),
                     self.__makePip(Point(x+offset, y+offset), self.pipsize)]    

        self.onTable = [[], [3], [0,6], [0,3,6], [0,2,4,6],
                        [0,2,3,4,6], [0,1,2,4,5,6]]
        self.setValue(self.value)
        
    def __makePip(self, center, radius):
        pip = Circle(center, radius)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip       

    def setValue(self, value):
        for pip in self.pips:
            pip.setFill(self.background)

        for item in self.onTable[value]:
            self.pips[item].setFill(self.foreground)
