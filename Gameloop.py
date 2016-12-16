import GUI
import Spieler
class Game:
	
	def getValue(self, x, y):
		return self.field[x] [y]
		
	def setValue(self, x, y, Value):
		self.field[x][y] = Value
		self.window.setCoin(x,y,Value)
	
	def __init__(self):
		self.player1 = Spieler.Spieler('Hans','Red')
		self.player2 = Spieler.Spieler('Peter','Yellow')
		self.window = GUI.gui(7,6, self.player1.nick, self.player1.colour, self.player2.nick, self.player2.colour, scale=2)
		self.field = [[0 for i in range(7)] for x in range(6)]
		print (self.field)
		


		
		
		
game = Game()

