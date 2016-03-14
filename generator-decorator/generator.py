#!/usr/bin/python

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1


 
a = counter_generator(5,10)

print a
"""<generator object counter_generator at 0x10f963be0>"""

for i in a:
	print i
"""
5
6
7
8
9
10
"""

