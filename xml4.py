#!/usr/bin/python
import urllib
import xml.etree.ElementTree as ET

#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_170258.xml'
#while True:
#    address = raw_input('Enter location: ')
#    if len(address) > 1 : break
print 'Retrieving', url
fh = urllib.urlopen(url)
data = fh.read()
print data
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
lst = tree.findall('comments/comment/count')
names = tree.findall('comments/comment/name')
results = sum(int(x.text) for x in lst)
print 'Count:', len(lst)
print 'Sum:', results
#for x in results:
#    print x.text
my_list = []
#print names
#print lst
print len(names)
print len(lst)
for a,b in zip(lst,names):
   my_list.append((a.text,b.text))

## Now get list of first 10 with maximyum count
for i in my_list[:10]:
	print i[1], i[0]
fh.close()


