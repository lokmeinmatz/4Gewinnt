import GUI
import Spieler
#from functools import partial
import random

class Game:
    
    def getValue(self, x, y):
        return self.field[x] [y]
        
    def setValue(self, x, y, Value):
        self.field[y][x] = Value
        self.window.setCoin(x,y,Value)


        
    
    def __init__(self):
        print("Spiel startet")
        #die beiden Spielerobjekte, speichern Nick und Farbe
        self.sp1 = Spieler.Sp("Peter", "yellow")
        self.sp2 = Spieler.Sp("Kevin", "green")

        #Waehlt zufaelligen Startspieler aus
        self.activeplayer = self.sp2
        if random.randint(0, 1) == 0:
            self.activeplayer = self.sp1

        self.window = GUI.gui(7, 6, spieler1=self.sp1, spieler2=self.sp2, active=self.activeplayer, scale=2)
        self.field = [[0 for i in range(7)] for x in range(6)]
        self.setAddCoinCommand()

    def addCoin(self, x):
        print(x)

        #wechsel zwischen sp1 und sp2
        if self.activeplayer == self.sp1:
            self.setValue(x, 2, 1)
            self.window.setAAAKTIVERplayer(self.sp2.nick)
            self.activeplayer = self.sp2

        elif self.activeplayer == self.sp2:
            self.setValue(x, 2, 2)
            self.window.setAAAKTIVERplayer(self.sp1.nick)
            self.activeplayer = self.sp1

    def setAddCoinCommand(self):
        self.window.setCoinCommand(self.addCoin)
        print(self.addCoin)
        self.window.window.mainloop()

    def checkforWin(self):
        for coin in self.field:
            #check tiles
            pass
        
        
        
    def Gameloop(self):
        print("Game started")


game = Game()

