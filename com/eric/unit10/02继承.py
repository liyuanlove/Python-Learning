class Animal:
	def run(self):
		print("animal is running")


class Cat(Animal):
	def __init__(self, name):
		self._name = name


mimi = Cat("mimi")
mimi.run()
isinstan = isinstance(mimi,Cat)
print(isinstan)