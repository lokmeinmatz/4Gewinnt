import tkinter as tk
import Spieler
import Gameloop

def updateColorp2(x):
    print(x)
    p2COLOR.config(bg=p2COLORvar.get())
    
def updateColorp1(x):
    print(x)
    p1COLOR.config(bg=p1COLORvar.get())



launcher = tk.Tk()
launcher.minsize(width=350, height=100)
launcher.title("4Gewinnt™ Launcher")


p1BOX = tk.Frame(launcher)

pl1LABEL = tk.Label(p1BOX, text="Spieler 1")
pl1LABEL.pack(side=tk.LEFT)



p1COLORvar = tk.StringVar(p1BOX)
p1COLORvar.set("blue")
p1COLOR = tk.OptionMenu(p1BOX, p1COLORvar, "blue", "red", "chocolate", "yellow", "gold", "lime green", "purple", command=updateColorp1)
p1COLOR.pack(side=tk.RIGHT)

p1NAME = tk.Entry(p1BOX)
p1NAME.pack(side=tk.RIGHT)

p1BOX.pack()

p2BOX = tk.Frame(launcher)

pl2LABEL = tk.Label(p2BOX, text="Spieler 2")
pl2LABEL.pack(side=tk.LEFT)



p2COLORvar = tk.StringVar(p2BOX)
p2COLORvar.set("blue")
p2COLOR = tk.OptionMenu(p2BOX, p2COLORvar, "blue", "red", "chocolate", "yellow", "gold", "lime green", "purple", command=updateColorp2)
p2COLOR.pack(side=tk.RIGHT)

p2NAME = tk.Entry(p2BOX)
p2NAME.pack(side=tk.RIGHT)

p2BOX.pack()




def startGame():
    
    p1 = Spieler.Sp(p1NAME.get(), p1COLORvar.get(), 1)
    
    p2 = Spieler.Sp(p2NAME.get(), p2COLORvar.get(), 2)
    launcher.destroy()
    
    print("start Spiel mit Spielern: "+p1.nick+" und " + p2.nick)
    game = Gameloop.Game(p1, p2)
    #hier dann das Objekt 4gewinnt erstellen mit boolean terminal = true/false

startbutton = tk.Button(launcher, text="Start", command=startGame)
startbutton.pack(side=tk.BOTTOM)

launcher.mainloop()