#!/usr/bin/python


def f1():
   print "This is function 1"

def f2():
   print "This is function 2"
   return f1()
   print "After calling function1"


f2()
