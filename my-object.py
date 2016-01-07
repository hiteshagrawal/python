#!/usr/bin/python

class PartyAnimal:
	#x = 0
	#name = ""
	def __init__(self,nam):
		self.x = 0
		self.name = nam
		print self.name, "I am constructed"

	def party(self):	
		self.x += 1
		print self.name,"So far", self.x

	def __del__(self):
		print self.name, "I am destructed", self.x


an = PartyAnimal("Hitesh")

an.party()
an.party()
an.party()	

ab = PartyAnimal("Naresh")	
ab.party()
an.party()
ab.party()

#Extending, Inheriting the partyanimal class
class FootballFan(PartyAnimal):
	points = 0
	def touchdown(self):
		self.points += 7
		self.party()
		print self.name, "points", self.points


ac = FootballFan("Nidhi")
ac.touchdown()
