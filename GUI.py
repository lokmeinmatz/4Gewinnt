import tkinter as tk
from functools import partial


class gui:

    def setScale(self, scale):
        self.scale = scale

    def setCoin(self, x, y, value):
        self.fieldarray[y][x] = value
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

    def initField(self, fieldarray):
        self.fieldarray = fieldarray
        self.canvas.create_rectangle(0, 0, self.breite*50*self.scale, self.leange*50*self.scale, fill="blue")


    def addCoinCallback(self, x):
        print("Ein Chip wurde in Reihe "+str(x)+" hinzugefuegt")

    def __init__(self, x, y, spieler1name, spieler1farbe, spieler2name, spieler2farbe, scale):
        self.setScale(scale)
        self.breite = x
        self.leange = y
        self.sp1color = spieler1farbe
        self.sp2color = spieler2farbe
        self.window = tk.Tk()
        self.window.title("Bestes Spiel")

        self.spieleristdrann = tk.Label(self.window, text="Spieler "+spieler1name+" ist drann")
        self.spieleristdrann.pack(side=tk.TOP)
        self.buttonframe = tk.Frame(self.window, width=x*50*self.scale)
        #die add buttons
        for i in range(x):
            #partial laesst der Funktion Argumente hinzufuegen
            tempbuttonframe = tk.Frame(self.buttonframe, width=50*scale, height=20)
            tempbuttonframe.pack(side=tk.LEFT)
            tempbuttonframe.pack_propagate(False)   

            button = tk.Button(tempbuttonframe, text="+", command=partial(self.addCoinCallback, i))
            button.pack()
            #button.place(bordermode=tk.OUTSIDE, x=x*50*self.scale, y=0, height=20, width=)

        self.buttonframe.pack(pady=10)

        #spielfeld
        self.canvas = tk.Canvas(self.window, width=x*50*self.scale, height=y*50*self.scale)
        self.canvas.pack(side=tk.BOTTOM)

        #malt das blaue HG-Feld und fuellt einen Array mit den Chips(circle-positions)
        field = [[0 for i in range(x)]for j in range(y)]

        self.initField(field)

        for xx in range(0, x):
            for yy in range(0, y):

                self.setCoin(xx, yy, 0)

        self.setCoin(2, 3, 1)

        self.window.mainloop()

window = gui(10, 5, spieler1name="Peter",spieler1farbe="yellow", spieler2name="Kevin", spieler2farbe="green", scale=3)
