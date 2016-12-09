import tkinter as tk



launcher = tk.Tk()

feldgrLabel = tk.Label(launcher, text="Feldgröße")
feldgrLabel.pack(side=tk.TOP)

breite = tk.Entry(launcher)
breite.pack(side = tk.LEFT)

xLabel = tk.Label(launcher, text="x")
xLabel.pack(side=tk.LEFT)

hoehe = tk.Entry(launcher)
hoehe.pack(side = tk.LEFT)

playmitGUI = tk.Checkbutton(launcher, text="Mit GUI spielen ")
playmitGUI.pack()


def startGame():
    x = breite.get()
    y = hoehe.get()
    print("start Spiel mit Feldgroesse: "+x+" x " + y)
    
    #hier dann das Objekt 4gewinnt erstellen mit boolean terminal = true/false

startbutton = tk.Button(launcher, text="Start", command=startGame)
startbutton.pack(side=tk.BOTTOM)

launcher.mainloop()