#!/usr/bin/python
## Square a number without using * or ^ sign

def square(number):
	total = 0
	for i in xrange(number):
		total += number
	return total
	
print square(7)	
print square(10)	
print square(25)		