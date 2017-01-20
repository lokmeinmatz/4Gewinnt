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

        #Felder in x und y , Variabel, sielfeld wird dementsprechend groesser, kleiner
        #Falls Nicht mehr alle Felder sichtbar sind, x und y reduzieren oder bei der GUI-Erstellung (s. self.window = GUI)
        #scale kleiner machen
        self.x = 7
        self.y = 6

        self.win = False

        self.window = GUI.gui(self.x, self.y, spieler1=self.sp1, spieler2=self.sp2, active=self.activeplayer, scale=2.5)
        self.field = [[0 for i in range(self.x)] for j in range(self.y)]




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
        self.window.setAAAKTIVERplayer(self.activeplayer)
        self.window.winnerbox.destroy()
    

    def checkforWin(self):
    
        #print fuer debugging
        for y in range(len(self.field)):
            #loop durch jede Zeile >> printe Zeile fue Debugging
            row = self.field[y]
            print(row)
            
        #ueberpruefen ob feld komplett voll ist
        feldleer = False
        for row in self.field:
            for coin in row:
                if coin == 0:
                    feldleer = True
                    break;
        
        if not feldleer:
            print("Spielfeld ist voll. keiner hat gewonnen")
            self.window.openNoWinnerBOX(self.restart)
            self.win = True
    
        # die Ueberpruefung ob und wer gewonnen hat
        #verbesserter Algorithmus als vorher, für alten siehe GitHub
        for y in range(len(self.field)):
            #loop durch jede Zeile >> bie einem Stein != 0 alle Felder neben, diagonal hoch und oben uueberpruefen
            row = self.field[y]
            

            for x in range(len(row)):
                # Nur ueberpruefen wenn Feld nicht leer ist
                if not self.getValue(x, y) == 0:
                    print("check "+str(self.getValue(x, y))+" at "+str(x)+" "+str(y))

                    #Koordinaten ab denen man nach vorne, unten , diagonal prueft


                    #Variablen die immer 1 Hoch zaehlen
                    tempx = x
                    tempy = y
                    player = self.getValue(x, y)
                    counterdown = 1
                    counterright = 1
                    counterdiagoup = 1
                    counterdiagodown = 1

                    while self.getValue(tempx, tempy) == player and not self.win:
                        #zaehlt wie viele Chips von dem Player in nach rechts einer Reihe sind
                        if tempx < 0 or tempx > self.x or tempy < 0 or tempy > self.y:
                            break
                        if self.getValue(tempx+1, tempy) == player:
                            counterright += 1
                            tempx += 1
                            print("--+1 nach rechts")
                        else:
                            print("nach rechts nix")
                            break

                    #reset der Koordinaten zum "Ausgangsfeld"
                    tempx = x
                    tempy = y

                    while self.getValue(tempx, tempy) == player and not self.win:
                        # zaehlt wie viele Chips von dem Player diagonal nach oben sind
                        if tempx < 0 or tempx > self.x or tempy < 0 or tempy > self.y:
                            break
                        
                        if self.getValue(tempx + 1, tempy - 1) == player:
                            counterdiagoup += 1
                            tempx += 1
                            tempy -= 1
                            print("--+1 nach diaup")
                        else:
                            print("nach diaup nix")
                            break

                    # reset der Koordinaten zum "Ausgangsfeld"
                    tempx = x
                    tempy = y

                    while self.getValue(tempx, tempy) == player and not self.win:
                        # zaehlt wie viele Chips von dem Player diagonal nach unten sind
                        if tempx < 0 or tempx > self.x or tempy < 0 or tempy > self.y:
                            break
                        if self.getValue(tempx + 1, tempy + 1) == player:
                            counterdiagodown += 1
                            tempx += 1
                            tempy += 1
                            print("--+1 nach diadown")
                        else:
                            print("nach diadown nix")
                            break

                    # reset der Koordinaten zum "Ausgangsfeld"
                    tempx = x
                    tempy = y

                    while self.getValue(tempx, tempy) == player and not self.win:
                        # zaehlt wie viele Chips von dem Player nach unten in einer Reihe sind
                        if tempx < 0 or tempx > self.x or tempy < 0 or tempy > self.y:
                            break
                        if self.getValue(tempx, tempy + 1) == player:
                            counterdown += 1
                            tempy += 1
                            print(str(tempx)+" "+str(tempy)+"--+1 nach unten")
                        else:
                            print("nach unten nix")
                            break


                    #ueberpruefungsalgorythmus
                    #fuer jeden chip wir ueberprueft, ob der chip rechts, unten diagonal unten(rechts) oder diagonal oben rechts von dem gleichen spieler ist.
                    #wenn ja, wird de jeweilige counter um 1 erhoeht und die temporaeren Koordinaten auf diesen neuen Chip gesetzt.
                    #wenn iener der counter >= 4 ist. hat der spieler 4 oder mehr in einer Reihe, da der Counter fuer jeden Chip
                    #zurueckgesetzt wird.
                    #Um Zickzack-Muster nicht zu zaehlen, sind dies individuelle while-loops.


                    if counterdown >= 4:
                        print("Gewonnen hat "+self.activeplayer.nick+" mit senkrecht")
                        self.window.openWinnerBOX(self.activeplayer, self.restart)
                        self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                        self.win = True
                        break
                    elif counterright >= 4:
                        print("Gewonnen hat "+self.activeplayer.nick+" mit waagerecht")
                        self.window.openWinnerBOX(self.activeplayer, self.restart)
                        self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                        self.win = True
                        break

                    elif counterdiagoup >= 4:
                        print("Gewonnen hat "+self.activeplayer.nick+" mit diagonal aufwaerts")
                        self.window.openWinnerBOX(self.activeplayer, self.restart)
                        self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                        self.win = True
                        break

                    elif counterdiagodown >= 4:
                        print("Gewonnen hat "+self.activeplayer.nick+" mit diagonal abwaerts")
                        self.window.openWinnerBOX(self.activeplayer, self.restart)
                        self.window.setAAAKTIVERplayer(self.activeplayer.nick+" hat gewonnen.")
                        self.win = True
                        break

