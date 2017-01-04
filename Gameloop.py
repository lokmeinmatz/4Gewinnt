import GUI
import Spieler
#from functools import partial
import random
import time

class Game:
    
    def getValue(self, x, y):
        return self.field[y] [x]
        
    def setValue(self, x, y, Value):
        self.field[y][x] = Value
        self.window.setCoin(x,y,Value)


        
    
    def __init__(self):
        print("Spiel startet")
        #die beiden Spielerobjekte, speichern Nick und Farbe
        self.sp1 = Spieler.Sp("Peter", "yellow", 1)
        self.sp2 = Spieler.Sp("Kevin", "green", 2)

        #Waehlt zufaelligen Startspieler aus
        self.activeplayer = self.sp2
        if random.randint(0, 1) == 0:
            self.activeplayer = self.sp1

        #Feldgroessen
        self.x = 7
        self.y = 6

        self.window = GUI.gui(self.x, self.y, spieler1=self.sp1, spieler2=self.sp2, active=self.activeplayer, scale=2)
        self.field = [[0 for i in range(7)] for x in range(6)]
        self.setAddCoinCommand()

    def addCoin(self, x):



        #wenn ein Knopf gedrueckt wird

        #suche die neidrigste Position die frei ist,  d.h. die Endposition
        maxdown = 0
        while maxdown < self.y and self.getValue(x, maxdown) == 0:
            maxdown +=1

        #wenn maxdown an x != 0 ist >> Spielstein Feld belegt, ist dies tiefstes freies Feld + 1 >> 1 abziehen um Endposition zu ermitteln

        maxdown -= 1
        print(str(maxdown)+" ist das unterste freie Feld")
        if maxdown < 0:
            print("Diese Reihe ist bereits voll")
            return
        #animation
        animy = 0
        while animy < maxdown:
            animy += 1
            self.setValue(x, animy, self.activeplayer.nr)
            time.sleep(0.15)
            self.setValue(x, animy, 0)


        #wechsel zwischen sp1 und sp2
        if self.activeplayer == self.sp1:
            self.setValue(x, maxdown, 1)
            self.window.setAAAKTIVERplayer(self.sp2.nick)
            self.activeplayer = self.sp2

        elif self.activeplayer == self.sp2:
            self.setValue(x, maxdown, 2)
            self.window.setAAAKTIVERplayer(self.sp1.nick)
            self.activeplayer = self.sp1

        #test fuer die x-y Anordnung
        #print(self.getValue(2, x))

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

