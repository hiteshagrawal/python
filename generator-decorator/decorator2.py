#!/usr/bin/python
import inspect
## Graham Dumpleton created wrapt library , to give us the proper arguments needed for a decorator
## http://blog.dscpl.com.au/2014/01/how-you-implemented-your-python.html
def decorator(function):
	def inner(*args,**kwargs):
		print "Before"
		res = function(*args,**kwargs)
		print "After"
		inner.__doc__ = function.__doc__
		inner.__name__ = function.__name__
		return res
	return inner


def add(a,b):
	"""Function to add two values"""
 	print a + b

print add.__name__ ## This will return add
print add.__doc__
## This is before decorating
add(5,10)

## Way of decorating
# @decorator
# def add(a,b):
# 	print a + b	

# Another way of decorating below
add = decorator(add)


add(5,10)	

print add.__name__  ## (this will return inner)
print add.__doc__ 

print inspect.getargspec(add)