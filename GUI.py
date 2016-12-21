import tkinter as tk
from functools import partial
import Spieler

class gui:

    #die "normale" Funktion fuer das Coin einfuegen mit dieser Funktion setzen
    # gui.setCoinCommand(befehl ohne klammern)
    
    def setCoinCommand(self, function, value):
        self.command = partial(function, value)

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
            fill_color = self.sp1color
        elif value == 2:
            fill_color = self.sp2color
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
        

    def __init__(self, x, y, spieler1name, spieler1farbe, spieler2name, spieler2farbe, scale, cmd):
    
        self.command = None
        
        self.setScale(scale)
        self.breite = x
        self.leange = y
        self.sp1color = spieler1farbe
        self.sp2color = spieler2farbe
        self.window = tk.Tk()
        self.window.title("© Mohhamad Karimba")
        self.window.iconbitmap(r"28trumpbelgium-web2-facebookJumbo.ico")
        self.spieleristdrann = tk.Label(self.window, text="Spieler "+spieler1name+" ist drann")
        self.spieleristdrann.pack(side=tk.TOP)
        self.buttonframe = tk.Frame(self.window, width=x*50*self.scale)
        #die add buttons
        for i in range(x):
            #partial laesst der Funktion Argumente hinzufuegen
            tempbuttonframe = tk.Frame(self.buttonframe, width=50*scale, height=20)
            tempbuttonframe.pack(side=tk.LEFT)
            tempbuttonframe.pack_propagate(False)   

            button = tk.Button(tempbuttonframe, text="+", command=partial(cmd, i))
            button.pack()
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

        

        self.window.mainloop()

      

def addCoin(x):
    print(x)

field = [[0 for i in range(7)] for x in range(6)]

player1 = Spieler.Spieler('Hans','Red')
player2 = Spieler.Spieler('Peter','Yellow')
	  
#Konstruktor, (Breite, Laenge, spielername 1, farbe spieler 1(auf Englisch), spielername 2, spieler 2 Farbe, Groese)
#window = gui(10, 5, spieler1name="Peter",spieler1farbe="yellow", spieler2name="Kevin", spieler2farbe="green", scale=2, cmd=addCoin)

#window.setCoinCommand(Null)