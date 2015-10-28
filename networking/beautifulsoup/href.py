#!/usr/bin/python
#pip install beautifulsoup4
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()  ### this is like a file read opeeration and html variable will contain a string
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags 
tags = soup('a')
for tag in tags:
	print tag.get('href', None)