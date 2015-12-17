#!/usr/bin/python
"""https://pr4e.dr-chuck.com/tsugi/mod/python-data/index.php?PHPSESSID=43bbd90447e2d6cfc811386aa0fa990e
Welcome Hitesh Agrawal from Using Python to Access Web Data

Following Links in Python

In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position from the top and follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Iria.html 
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Iria Freja Dre Franklin Ze 
Last name in sequence: Ze
Actual problem: Start at: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Narissa.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
First character of last name in sequence: J
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python solution.py 
Enter URL: http://pr4e.dr-chuck.com/ ... /known_by_Iria.html
Enter count: 4
Enter position: 3
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Iria.html
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Freja.html
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Dre.html
Retrieving: http://pr4e.dr-chuck.com/ ... /known_by_Franklin.html
Last Url: http://pr4e.dr-chuck.com/ ..../known_by_Ze.html
The answer to the assignment for this execution is "Ze".
"""
from BeautifulSoup import *
import urllib
url = raw_input("Enter URL: ")
count = int(raw_input("Enter Count: "))
position = int(raw_input("Enter postion: ")) - 1
print "Retrieving:", url
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
#print tags
#print "This is my data"
# print tags[position]
# print "This is my data 2"
# print tags[position].get('href', None)

for i in range(count):
	## print the contents specified at position
	mytag = tags[position].contents[0]
	#First get the new href
	newurl = tags[position].get('href', None)
	if i < count - 1 :	
		print "Retrieving:", newurl
		## Read the newurl as newhtml 
		newhtml = urllib.urlopen(newurl).read()
		## Convert the newhtml in beatifulsoup object
		soup = BeautifulSoup(newhtml)
		## Get all the tags with anchor a
		tags = soup('a')
	else:
		print "Last Url:", newurl
		print mytag	
