#!/usr/bin/python
"""Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Kaia.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: R"""

from BeautifulSoup import *
import urllib
url = raw_input("Enter URL: ")
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = int(raw_input("Enter Count: ")) 
#count = 4
#position = 3
position = int(raw_input("Enter position: ")) - 1 
# print "Retrieving:", url
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
# tags = soup('a')
# print tags[]
# print tags[2].contents[0]
#for tag in tags:
#	print tag[3]
def retrive(url,count,position):
	if count > 0:
		print "Retrieving:", url
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)
		tags = soup('a') 
		print tags[position].contents[0] ## Coz position starts from index 0
		newurl = tags[position].get('href', None)
		count -= 1
		retrive(newurl,count,position)

retrive(url,count,position)	
