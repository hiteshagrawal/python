#!/usr/bin/python

a = range(10)

print a
even = []
odd = []
for i in range(len(a)/2):
	odd.append(a.pop())
	even.append(a.pop())
	
print even
print odd	

a = range(10)

even = [x for x in a[::2]]
odd = [x for x in a[1::2]]
print even
print odd
