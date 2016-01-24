#!/usr/bin/python
"""How do you remove repeated values from a INT array, returning the resultant array in the same order as original ?
"""

a = [1,2,3,4,4,4,5,8,8,6,6,3,3,4,4]
print a

def remove_duplicate(my_list):
	new_list = [my_list.pop(0)]
	for i in my_list:
	    if i != new_list[-1]:
	        new_list.append(i)
	print new_list

remove_duplicate(a) 