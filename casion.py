import random

class Deck(object):
	def shuffle(self):
		suits = ["Spades","Clubs","Diamonds","Hearts"]
		ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
		self.cards = []
		for suit in suits:
			for rank in ranks:
				self.cards.append(rank + " of " + suit)
		random.shuffle(self.cards)

	def draw(self):
		return self.cards.pop()

d = Deck()
d.shuffle()
print(d.draw())
print(d.draw())
print(d.draw())
