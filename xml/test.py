#!/usr/bin/python
import urllib
url = 'https://docs.python.org/2/library/xml.etree.elementtree.html'

connection = urllib.urlopen(url)
data = connection.read()
headers = connection.info().dict

print data
print headers