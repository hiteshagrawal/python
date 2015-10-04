#!/usr/bin/python
try:
   fh = open("file1.txt","r")
except:
   print "You entered a invalid file"
   exit()

a = fh.read()
print a
fh.close()
