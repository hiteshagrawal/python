#!/usr/bin/python
import re
print sum( [ int(x) for x in re.findall('[0-9]+', open('sum.txt').read()) ] ) ## This will sum a list
print sum(int(x) for x in re.findall('[0-9]+', open('sum.txt').read())) ## This will create a generator and then sum it

a = (int(x) for x in re.findall('[0-9]+', open('sum.txt').read()))
print type(a)
