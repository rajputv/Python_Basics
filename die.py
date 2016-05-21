import random
class Die(object):
	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return random.randint(1, self.sides)

print("6 sided die:")
d = Die(6)
print(d.roll())
print(d.roll())
print(d.roll())
print("")
print("20 sided die:")
d = Die(20)
print(d.roll())
print(d.roll())
print(d.roll())
