#!/usr/bin/python

def add10(x):
	"""
	Adds 10 to the input value
	## Comments starting with # are ignored
	>>> foo = "bar"
	>>> foo  ##"Implicit print"
	'bar'
	>>> print foo  ##"Explicit print"
	bar
	>>> add10(5)
	15
	>>> add10(-2)
	8
	>>> add10(-20)
	-10
	"""
	return x + 10

if __name__ == "__main__":
	import doctest
	print doctest.testmod()	