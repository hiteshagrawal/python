#!/usr/bin/python
#pip install beautifulsoup4
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()  ### this is like a file read opeeration and html variable will contain a string
soup = BeautifulSoup(html, "html.parser")  ## to parse the above string as html data
# Retrieve all of the anchor tags 
tags = soup('a')  ### This will retrieve all the <a  .... /a> from the html
print tags  ## This will print the list with all the anchor tags , below we are going to fet the href
for tag in tags:
	print tag.get('href', None)