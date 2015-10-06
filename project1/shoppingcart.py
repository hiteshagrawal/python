#!/usr/bin/python

import random
done = False

class ShoppingCart:
	def __init__(self):
		self.items = []

	def addtocart(self,item):
		self.items.append(item)

	def removefromcart(self,itemindex):
		self.items.pop(itemindex)

	def pricecart(self):
		price = 0
		for item in self.items:
			price += item.price
		return price
		
	def listcart(self):
		cid = 0
		print "Cart Items:"
		print "Item      Price     CartID"
		for x in self.items:
			print x.name, x.price, cid	
			cid += 1
		print ""
		
class Item:
	def __init__(self, price, name):
		self.price = price
		self.name = name

store = []
itemnames = ["HDMI Cable", "Keyboard", "Headphones", "RAM"]

def makeStoreItems(amt):
	storeitems = 0
	while storeitems <= amt:
		nItem = Item(random.randrange(51), random.choice(itemnames))
		store.append(nItem)
		storeitems += 1

# makeStoreItems(3)
# for x in store:
# 	print x.name, x.price

def CreateStore(storefile):
	try:
		fx = open(storefile,'r')
	except IOError:
		print "No Existing Store.. generating items"
		makeStoreItems(4)

## List all the items in the store
def liststore():
	iid = 0  ## Item id
	print "Itemid    ItemPrice     ItemName"
	for x in store:
		print iid, x.price, x.name
		iid += 1		

def printInstructions():
	print "Type C to view your cart items"
	print "Type R to remove your cart items"
	print "Type an item number to buy"
	print "Type P to get the total cart price"
	print "Type x to exit"

def removeItem(cart):
	input1 = input("Type a cart object ID to remove")
	cart.removefromcart(input1)

def handleInput(in_var,cart):
	char_inputs = ["C", "R" , "P", "X"]
	if in_var.upper() == "C":
		cart.listcart()
	if in_var.upper() == "R":
		removeItem(cart)
	if in_var.upper() == "P":
		print "The items in your cart currently cost"
		print cart.pricecart()
	if in_var.upper() == "X":
		global done
		done = True	
	if in_var.upper() not in char_inputs:
		try:
			cart.addtocart(store[int(in_var)])
		except:
			print "You specified an illegal character!"		
			
#makeStoreItems(4)
#liststore()

cart1 = ShoppingCart()
CreateStore("cart1")
while (done == False):
	liststore()
	printInstructions()
	input_var = raw_input("Enter the item to buy (type the id):")
	handleInput(input_var,cart1)
