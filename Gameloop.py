from builtins import print

import GUI
import Spieler
#from functools import partial
import random

class Game:
    
    def getValue(self, x, y):
        try:
            return self.field[y] [x]
        except IndexError :
            return 0


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

        self.x = 7
        self.y = 6


        self.window = GUI.gui(self.x, self.y, spieler1=self.sp1, spieler2=self.sp2, active=self.activeplayer, scale=2)
        self.field = [[0 for i in range(7)] for x in range(6)]




        self.setAddCoinCommand()


    def addCoin(self, x):



        print("Ein Chip wurde in "+str(x)+" eingeworfen.")

        maxdown = 0;
        while maxdown < self.y and self.getValue(x, maxdown) == 0:
            maxdown += 1


        #-1 um nicht das erste belegte feld zu finden sondern das letzte leere
        maxdown -= 1


        #wenn die Reihe voll ist, d.h. der maxdown counter nicht runterehen kann
        if maxdown < 0:
            print("Diese Reihe ist bereits voll")
            #durch return wird der Rest nichtmehr ausgefuehrt
            return

        #Wechsel zwischen spieler1 und spieler2
        if self.activeplayer == self.sp1:
            self.setValue(x, maxdown, 1)
            self.window.setAAAKTIVERplayer(self.sp2.nick)
            self.activeplayer = self.sp2

        elif self.activeplayer == self.sp2:
            self.setValue(x, maxdown, 2)
            self.window.setAAAKTIVERplayer(self.sp1.nick)
            self.activeplayer = self.sp1


        self.checkforWin()

    def setAddCoinCommand(self):
        self.window.setCoinCommand(self.addCoin)
        print(self.addCoin)
        self.window.window.mainloop()

    def checkforWin(self):
        # die Ueberpruefung ob und wer gewonnen hat
        for y in range(len(self.field)):
            #loop durch jede Zeile >> bie einem Stein != 0 alle Felder neben, diagonal hoch und oben uueberpruefen
            row = self.field[y]
            print(row)

            for x in range(len(row)):
                if not self.getValue(x, y) == 0:
                    print("check "+str(self.getValue(x, y))+" at "+str(x)+" "+str(y))

                    tempx = x
                    tempy = y
                    #ueberpruefungsalgorythmus







        
        
        
    def Gameloop(self):
        print("Game started")


game = Game()

