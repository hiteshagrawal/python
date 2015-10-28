#!usr/bin/python
import urllib
fh = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

print type(fh)
print fh
print fh.read()
fh.close()
#for line in fh:
#	print line.strip()
## you can use the wordcount program on top of this and do whatever you want , the fh is just like a file handle 
#and it returns the data in string format when you apply read method to it
print urllib.urlopen('http://www.py4inf.com/code/romeo.txt').read()

#https://www.coursera.org/learn/python-network-data/exam/lFRgx/networks-and-sockets
