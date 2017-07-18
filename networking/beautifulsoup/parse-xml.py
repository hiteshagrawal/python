#!/usr/bin/python

"""

"""
import urllib
import xml.etree.ElementTree as ET


while True:
    url = raw_input('Enter location: ')
    if len(url) > 1 : break

#url =  'http://py4e-data.dr-chuck.net/comments_42.xml'    

print "Retrieving " + url
data = urllib.urlopen(url).read()
print "Retrieved %d characters" %(len(data))
tree = ET.fromstring(data)
results = tree.findall('comments/comment/count')
print "Count :%d" %(len(results))
#for item in results:
#	print item.text

print "The Sum is: %d" % (sum(int(x.text) for x in results))