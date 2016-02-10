#!/usr/bin/python
"""

"Smart substring" 
Write a function that takes maximum 30 characters from a string but without cutting the words. 

Full description: 
"Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam." 

First 30 characters: 
"Featuring stylish rooms and mo" 

Smarter approach (max 30 characters, no words are broken): 
"Featuring stylish rooms and"
"""
a = "Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam." 
#print a
#print a.find("moorings")  ## This returns 28
#print a.find("for") 
#print a[:30]  ## This returns Featuring stylish rooms and mo
new_str = ""
def smart_string(my_string):
	global new_str
	my_list = my_string.split()
	while True:
		if len(new_str + my_list[0]) <= 30:
			new_str += my_list.pop(0) + " "
		else:
			return new_str 

print smart_string(a)