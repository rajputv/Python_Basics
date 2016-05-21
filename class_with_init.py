#init will always be called when a class is initiated
class Greeter(object):
	def __init__(self, name):
		self.name = name
	def hello(self):
		print("Hello " + self.name)
	def goodbye(self):
		print("Goodbye " + self.name)

g = Greeter("vivek")
g.hello()
g.goodbye()
print("")
g2 = Greeter("akshay")
g2.hello()
g2.goodbye()
