#!/usr/bin/python
import re

fd = open('passwd', 'rb')

print type(fd)
a = fd.read()
x = [ y for y in re.findall(':', a) ]
print "The number of fields in passwd file is",len(x)
uid = sum([ int(z) for z in re.findall('x:([0-9]+):', a) ])
print "The sum of uid is", uid
   
fd.close()