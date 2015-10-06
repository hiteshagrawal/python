#!/usr/bin/python

import random
done = False

class ShoppingCart:
	def __init__(self):
		## Initialize empty cart
		self.cart = []

	def addtocart(self, item):
		self.cart.append(item)

	def removefromcart(self, itemindex):
		if len(self.cart) != 0:
			self.cart.pop(itemindex)

	def listcart(self):
		cid = 0
		print "CID  PRICE    NAME"
		for item in self.cart:
			print cid, item.price, item.name
			cid += 1

	def getprice(self):
		price = 0
		for item in self.cart:
			price += item.price
		print "Your cart price is:", price	


class Item:
	def __init__(self, price, name):
		self.price = price
		self.name = name


store = []
storeitems = ["Dal", "Rice", "Veg", "Roti", "Paneer", "Butter"]
my_shoppingcart = ShoppingCart()


def MakeStore(amt):
	counter = 0
	while counter < int(amt):
		nItem = Item(random.randrange(51), random.choice(storeitems))
		store.append(nItem)
		counter += 1

def listStore():
	sid = 0
	print "SID  PRICE    NAME"
	for x in store:
		print sid, x.price, x.name
		sid += 1

def handle_input(cart):
	global done
	
	print "Type C to view your Cart"
	print "Type R to Remove item from your Cart"
	print "Type an item number to add item to your cart"
	print "Type P to get the total of your Cart"
	print "Type X to exit"
	my_input = raw_input("Enter your choice:")
	if my_input.upper() == "C":
		cart.listcart()
	elif my_input.upper() == "R":
		remove_item = input("Enter item index id to remove:")
		cart.removefromcart(remove_item)
	elif my_input.upper() == "P":
		cart.getprice()
	elif my_input.upper() == "X":
		done = True
	else:	
		cart.addtocart(store[int(my_input)])
	print ""	
     
MakeStore(4)
#listStore()

my_shoppingcart = ShoppingCart()
#my_shoppingcart.addtocart(store[0])

#my_shoppingcart.listcart()

while done == False:
	listStore()
	handle_input(my_shoppingcart)


		
		

