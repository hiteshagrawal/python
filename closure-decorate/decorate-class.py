#!/usr/bin/python

def outer_function():
	message = "hi"
	def inner_function():
		print(message)
		#return 1

	return inner_function
	
my_func = outer_function()		
#print my_func()
print my_func()

def decorate_feature(f):
	def inner(**kwargs):
		f.weight = kwargs['weight']
		return f(kwargs['color'],kwargs['height'])
	return inner


class Feature:
	def __init__(self, color, height):
		self.color = color
		self.height = height


hitesh = Feature(color='brown',height=33)

print hitesh.color
print hitesh.height

## Now decorate our original Feature class to accept a weight attribute too
Feature = decorate_feature(Feature)

naresh = Feature(color='brown',height='33cm',weight='68kgs')	

print naresh.weight





