#!/usr/bin/python


def f1():
   print "This is function 1"

def f2():
   print "This is function 2"
   return f1()
   print "After calling function1"


f2()

a = "networking"
n = ""
for i in a:
	n += i + " "
	#print n
print n	
print " Printing lambda output"
print reduce(lambda a, b: a + " " + b, "networking")
print "Printing join output"
print " ".join(list(a))