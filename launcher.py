import tkinter as tk
import Spieler
import Gameloop



def updateColorp2(x):
    global lastp2Color
    if not p2COLORvar.get() == p1COLORvar.get():
        print(x)
        p2COLOR.config(bg=p2COLORvar.get())
        lastp2Color = p2COLORvar.get()
    else:
        p2COLORvar.set(lastp2Color)

    
def updateColorp1(x):
    global lastp1Color
    if not p1COLORvar.get() == p2COLORvar.get():
        print(x)
        p1COLOR.config(bg=p1COLORvar.get())
        lastp1Color = p1COLORvar.get()
    else:
        p1COLORvar.set(lastp1Color)

        
lastp1Color = "red"
lastp2Color = "yellow"

launcher = tk.Tk()
launcher.minsize(width=350, height=100)
launcher.title("4Gewinnt™ Launcher")


p1BOX = tk.Frame(launcher)

pl1LABEL = tk.Label(p1BOX, text="Spieler 1")
pl1LABEL.pack(side=tk.LEFT)



p1COLORvar = tk.StringVar(p1BOX)
p1COLORvar.set("red")
p1COLOR = tk.OptionMenu(p1BOX, p1COLORvar, "red", "chocolate", "yellow", "gold", "lime green", "purple", command=updateColorp1)
p1COLOR.pack(side=tk.RIGHT)
p1COLOR.config(bg=p1COLORvar.get())

p1NAME = tk.Entry(p1BOX)
p1NAME.pack(side=tk.RIGHT)

p1BOX.pack()

p2BOX = tk.Frame(launcher)

pl2LABEL = tk.Label(p2BOX, text="Spieler 2")
pl2LABEL.pack(side=tk.LEFT)



p2COLORvar = tk.StringVar(p2BOX)
p2COLORvar.set("yellow")
p2COLOR = tk.OptionMenu(p2BOX, p2COLORvar, "red", "chocolate", "yellow", "gold", "lime green", "purple", command=updateColorp2)
p2COLOR.pack(side=tk.RIGHT)
p2COLOR.config(bg=p2COLORvar.get())

p2NAME = tk.Entry(p2BOX)
p2NAME.pack(side=tk.RIGHT)

p2BOX.pack()




def startGame():
    if p1NAME.get()and p2NAME.get() and not p1NAME.get() == p2NAME.get():
        p1 = Spieler.Sp(p1NAME.get(), p1COLORvar.get(), 1)
        
        p2 = Spieler.Sp(p2NAME.get(), p2COLORvar.get(), 2)
        launcher.destroy()
        
        print("start Spiel mit Spielern: "+p1.nick+" und " + p2.nick)
        game = Gameloop.Game(p1, p2)
    #hier dann das Objekt 4gewinnt erstellen mit boolean terminal = true/false

startbutton = tk.Button(launcher, text="Start", command=startGame)
startbutton.pack(side=tk.BOTTOM)

launcher.mainloop()