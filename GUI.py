import tkinter as tk


class gui:
    def __init__(self, x, y, spieler1name, spieler2name):
        self.breite = x
        self.leange = y
        self.window = tk.Tk()
        self.window.title("Bestes Spiel")
        
        self.spieleristdrann = tk.Label(self.window, text="Spieler "+spieler1name+" ist drann")
        self.spieleristdrann.pack(side=tk.TOP)
        self.buttonframe = tk.Frame(self.window)
        #die add buttons
        for i in range(x):
            button = tk.Button(self.buttonframe, text="    +    ")
            button.pack(side=tk.LEFT)
        
        self.buttonframe.pack()
        
        #spielfeld
        canvas = tk.Canvas(self.window, width=x*50, height=y*50)
        canvas.pack()
        
        self.window.mainloop()
        # macht hinzufuegenbuttons
        #for
        
        
        
        
        
        
window = gui(5, 1, "Peter", "Kevin")