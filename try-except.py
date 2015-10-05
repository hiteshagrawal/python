#!/usr/bin/python

num1 = input("Enter a number:")
num2 = input("Enter another number:")

try:
	print num1/num2
except ZeroDivisionError:
	print "Dividing by zero"


raise ZeroDivisionError	