#!/usr/bin/python

import urllib
import xml.etree.ElementTree as ET

#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_170258.xml'
while True:
    address = raw_input('Enter location: ')
    if len(address) > 1 : break
print 'Retrieving', address
fh = urllib.urlopen(address)
data = fh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
lst = tree.findall('comments/comment/count')
names = tree.findall('comments/comment/name')
results = sum(int(x.text) for x in lst)
print 'Count:', len(lst)
print 'Sum:', results
#for x in results:
#    print x.text
my_dict = {}
#print names
#print lst
len(names)
len(lst)
#for a in names:
#   print a.text 
#for key,value in my_dict.items():
#    print key,value
fh.close()
