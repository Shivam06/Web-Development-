# Understanding use of **kwargs in class - keywords - arguments

class Animal:
	def __init__(self, **kwargs): # kwargs is a dictionary
		self._attributes = kwargs

	def set_attributes(self, key, value = "No Name"):
		self._attributes[key] = value

	def get_attributes(self, key):
		return self._attributes[key]

	def noise(self):
		print "err err!"

	def move(self):
		print "Move Forward"

"""dog = Animal(name = "Puppy")
print dog.get_attributes("name")
dog.set_attributes("noise","bhaoo")
print dog.get_attributes("noise")
dog.noise()
dog.move()"""

class Dog(Animal):
	def noise(self):
		print "bhaoo bhaoo"
		super(Dog,self).__init__()
		super(Dog).noise()
dog = Dog()
dog.noise()
