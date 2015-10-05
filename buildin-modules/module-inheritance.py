#!/usr/bin/python
# Below is SuperClass
class Vehicle():
	wheels = 4
	def __init__(self):
		print "Vehicle"
	def brake(self,x):
		return x * -10


# Below is the subclass and can access any function,variable of the parent/superclass
class Car(Vehicle):   ## This will inherite the wheels variable from the parent class Vehicle too
	def __init__(self):
		self.speed = 10

	def calcVelocity(self,x):
		return 3*x + 10

examplecar = Car()
print examplecar.speed   ### This will fetch speed variable and print 10
print examplecar.calcVelocity(10)  ## This will print 3*10+10 = 40
print examplecar.wheels  ## This will print 4
print examplecar.brake(2)  ## This will print 20 , we are now accessing brake function from the superclass via subclass
