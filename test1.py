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

a = xrange(10) # We have a generator now
print type(a)
#xrange(10)
print list(a)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print [x for x in list(a)[::2]]
#[0, 2, 4, 6, 8]
print [x for x in list(a)[1::2]]
#[1, 3, 5, 7, 9]
#>>> 

