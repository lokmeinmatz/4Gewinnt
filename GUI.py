import tkinter as tk
from functools import partial
import Spieler


class gui:

    #die "normale" Funktion fuer das Coin einfuegen mit dieser Funktion setzen
    # gui.setCoinCommand(befehl ohne klammern)
    
    def setCoinCommand(self, function):
        for i in range(self.breite):
            print(i)
            button = self.buttonarray[i]
            #partial: laess eine funktion von einem anderen Programm aufrufen und uebergibt dabei variablen
            button.configure(command=partial(function, i))

    def closeAll(self):
        self.winnerbox.destroy()
        self.window.destroy()

        
        
    def openWinnerBOX(self, player, restartcmd):
        self.winnerbox = tk.Toplevel()
        self.winnerbox.title(player.nick+" hat gewonnen")
        msg = tk.Message(self.winnerbox, text="Herzlichen Glückwunsch.").pack()
        msg2 = tk.Message(self.winnerbox, text=player.nick+" ist halt besser. Kann man nix machen.").pack()
        bttn = tk.Button(self.winnerbox, text="Spiel beenden", command=self.closeAll).pack()
        bttnrestart = tk.Button(self.winnerbox, text="Neues Spiel", command=restartcmd).pack()


    def setScale(self, scale):
        self.scale = scale

    def setCoin(self, x, y, value):
        #Benutzung:
        #x und y sind die Koordinaten in dem Feld welches verändert werden soll
        #abfragen sind nicht sinnvoll, die Martix hier ist nur fuer die Darstellung
    
        #Value: 0 malt Feld weiß, 1 malt Spielerfarbe 1 und 2 Spielerfarbe 2
        
        
        dx = (x + 1) * 50*self.scale - 4
        dy = (y + 1) * 50*self.scale - 4
        x = x*50*self.scale+4
        y = y*50*self.scale+4

        print(x, y, dx, dy)

        fill_color = ""
        if value == 0:
            fill_color = "white"
        elif value == 1:
            fill_color = self.sp1.colour
        elif value == 2:
            fill_color = self.sp2.colour
        else:
            fill_color = "red"

        self.canvas.create_oval(x, y, dx, dy, fill=fill_color)

    def initField(self):
    # malt den Hintergrund. wird von init aufgerufen, daher nicht noetig selbest aufzurufen
        self.canvas.create_rectangle(0, 0, self.breite*50*self.scale, self.leange*50*self.scale, fill="blue")


    def addCoinCallback(self, x):
        print("Ein Chip wurde in Reihe "+str(x)+" hinzugefuegt")
        
        #sollte die hinzufuegefunktion des normalen Programmes aufrufen
        # x ist die Reihe, mit partial - Funktion werte uebergeben
    
    def setAAAKTIVERplayer(self, name):
        self.spieleristdrann.configure(text="Spieler "+name+" ist drann")

    def __init__(self, x, y, spieler1, spieler2, active, scale):
    
        
        self.setScale(scale)
        self.breite = x
        self.leange = y
        self.sp1 = spieler1
        self.sp2 = spieler2
        self.window = tk.Tk()
        self.window.title("4Gewinnt™ 1.0")
        self.window.iconbitmap(r"Logo 4 Gewinnt.ico")
        self.spieleristdrann = tk.Label(self.window, text="Spieler "+active.nick+" ist drann")
        self.spieleristdrann.pack(side=tk.TOP)
        self.buttonframe = tk.Frame(self.window, width=x*50*self.scale)
        #die add buttons
        
        #array von buttons
        self.buttonarray = []
        
        for i in range(x):
            #partial laesst der Funktion Argumente hinzufuegen
            tempbuttonframe = tk.Frame(self.buttonframe, width=50*scale, height=20)
            tempbuttonframe.pack(side=tk.LEFT)
            tempbuttonframe.pack_propagate(False)   

            button = tk.Button(tempbuttonframe, text="+")
            button.pack()
            self.buttonarray.append(button)
            #button.place(bordermode=tk.OUTSIDE, x=x*50*self.scale, y=0, height=20, width=)

        self.buttonframe.pack(pady=10)

        #spielfeld
        self.canvas = tk.Canvas(self.window, width=x*50*self.scale, height=y*50*self.scale)
        self.canvas.pack(side=tk.BOTTOM)

        #malt das blaue HG-Feld und fuellt einen Array mit den Chips(circle-positions)
        self.initField()

        for xx in range(0, x):
            for yy in range(0, y):

                self.setCoin(xx, yy, 0)

        

        













	  
#Konstruktor, (Breite, Laenge, spielername 1, farbe spieler 1(auf Englisch), spielername 2, spieler 2 Farbe, Groese)

#window.setCoinCommand(Null)
