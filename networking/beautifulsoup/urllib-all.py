#!/usr/bin/python
# Pg :163 -- Python for Informatics
import urllib
from BeautifulSoup import *
#url = raw_input('Enter - ')
#url = "http://www.dr-chuck.com/page1.htm"
url = "http://www.py4inf.com/book.htm"
html = urllib.urlopen(url).read() 
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags 
tags = soup('a')
#print tags
for tag in tags:
	#Lookatthepartsofatag
	print 'TAG:',tag
	print 'URL:',tag.get('href', None) 
	print 'Content:',tag.contents[0] 
	print 'Attrs:',tag.attrs