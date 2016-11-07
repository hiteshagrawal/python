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

if __name__ == '__main__':
	ac = FootballFan("Nidhi")
	ac.touchdown()

class CricketFan(PartyAnimal):
	def __init__(self,nam,score):
		print("CricketFan Constructed")
		PartyAnimal.__init__(self,nam)
		self.score = score

	def cricketscore(self):
		self.score += 1
		print(self.name, "runs", self.score)

Avni = CricketFan("Avni",5)
Avni.cricketscore()		
		
class HockeyFan(PartyAnimal):
	#Exception AttributeError: "HockeyFan instance has no attribute 'name'" 
	#in <bound method HockeyFan.__del__ of <__main__.HockeyFan instance at 0x1004dbdd0>> ignored
	def __init__(self, nam, hscore):
		print("HockeyFan Constructed")
		PartyAnimal.__init__(self,nam)
		self.hscore = int(hscore)

	def hockeyscore(self):
		self.hscore += 1
		print "hockeyscore", self.hscore


yashvi = HockeyFan("Yashvi", 2)
yashvi.hockeyscore()		
		
