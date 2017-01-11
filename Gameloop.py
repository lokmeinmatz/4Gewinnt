from builtins import print

import GUI
import Spieler
#from functools import partial
import random

class Game:
    
    def getValue(self, x, y):
        try:
            return self.field[y] [x]
            #indexerror wenn abfrage ausserhalb vom Spielfeld
        except IndexError :
            return 0


    def setValue(self, x, y, Value):
        self.field[y][x] = Value
        self.window.setCoin(x,y,Value)


        
    
    def __init__(self, p1, p2):
        print("Spiel startet")
        #die beiden Spielerobjekte, speichern Nick und Farbe
        self.sp1 = p1
        self.sp2 = p2

        #Waehlt zufaelligen Startspieler aus
        self.activeplayer = self.sp2
        if random.randint(0, 1) == 0:
            self.activeplayer = self.sp1

        self.x = 7
        self.y = 6

        self.win = False

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
        if not self.win:
            self.setValue(x, maxdown, self.activeplayer.nr)





            self.checkforWin()

            if self.activeplayer == self.sp1:
                self.window.setAAAKTIVERplayer(self.sp2.nick)

                self.activeplayer = self.sp2

            elif self.activeplayer == self.sp2:
                self.setValue(x, maxdown, 2)
                self.window.setAAAKTIVERplayer(self.sp1.nick)
                self.activeplayer = self.sp1
        
        
            
        
            

    def setAddCoinCommand(self):
        self.window.setCoinCommand(self.addCoin)
        print(self.addCoin)
        self.window.window.mainloop()
        
        
    def restart(self):
        for x in range(len(self.field)):
            for y in range(len(self.field[1])):
                self.setValue(y, x, 0)
        
        self.win = False
                
        self.activeplayer = self.sp2
        if random.randint(0, 1) == 0:
            self.activeplayer = self.sp1
            
        self.window.winnerbox.destroy()
    

    def checkforWin(self):
    
        #print fuer debugging
        for y in range(len(self.field)):
            #loop durch jede Zeile >> bie einem Stein != 0 alle Felder neben, diagonal hoch und oben uueberpruefen
            row = self.field[y]
            print(row)
    
        # die Ueberpruefung ob und wer gewonnen hat
        for y in range(len(self.field)):
            #loop durch jede Zeile >> bie einem Stein != 0 alle Felder neben, diagonal hoch und oben uueberpruefen
            row = self.field[y]
            

            for x in range(len(row)):
                if not self.getValue(x, y) == 0:
                    print("check "+str(self.getValue(x, y))+" at "+str(x)+" "+str(y))


                    tempx = x
                    tempy = y
                    player = self.getValue(x, y)
                    counterdown = 1
                    counterright = 1
                    counterdiagoup = 1
                    counterdiagodown = 1
                    #ueberpruefungsalgorythmus
                    #fuer jeden chip wir ueberprueft, ob der chip rechts, unten diagonal unten(rechts) oder diagonal oben rechts von dem gleichen spieler ist.
                    #wenn ja, wird de jeweilige counter um 1 erhoeht und die temporaeren Koordinaten auf diesen neuen Chip gesetzt.
                    #wenn iener der counter >= 4 ist. hat der spieler 4 oder mehr in einer Reihe, da der Counter fuer jeden Chip
                    #zurueckgesetzt wird.

                    while self.getValue(tempx, tempy) == player and not self.win:
                        print("Player "+str(player)+" has coin at "+str(tempx)+" "+str(tempy))
                        if self.getValue(tempx+1, tempy) == player:
                            counterright += 1
                            tempx += 1
                        elif self.getValue(tempx+1, tempy+1) == player and counterright == 1 and counterdiagodown == 1 and counterdown == 1:
                            counterdiagoup += 1
                            tempx += 1
                            tempy += 1
                        elif self.getValue(tempx+1, tempy-1) == player and counterright == 1 and counterdiagoup == 1 and counterdown == 1:
                            counterdiagodown += 1
                            tempx += 1
                            tempy -= 1
                        elif self.getValue(tempx, tempy-1) == player and counterright == 1 and counterdiagoup == 1 and counterdiagodown == 1:
                            counterdown += 1
                            tempy -= 1
                        else:
                            break


                        if counterdown >= 4:
                            print("Gewonnen hat "+self.activeplayer.nick+" mit senkrecht")
                            self.window.openWinnerBOX(self.activeplayer, self.restart)
                            self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                            self.win = True
                            break
                        if counterright >= 4:
                            print("Gewonnen hat "+self.activeplayer.nick+" mit waagerecht")
                            self.window.openWinnerBOX(self.activeplayer, self.restart)
                            self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                            self.win = True
                            break

                        if counterdiagoup >= 4:
                            print("Gewonnen hat "+self.activeplayer.nick+" mit diagonal aufwaerts")
                            self.window.openWinnerBOX(self.activeplayer, self.restart)
                            self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                            self.win = True
                            break

                        if counterdiagodown >= 4:
                            print("Gewonnen hat "+self.activeplayer.nick+" mit diagonal abwaerts")
                            self.window.openWinnerBOX(self.activeplayer, self.restart)
                            self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                            self.win = True
                            break

