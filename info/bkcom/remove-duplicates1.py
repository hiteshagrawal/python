#!/usr/bin/python
"""How do you remove repeated values from a INT array, returning the resultant array in the same order as original ?
"""

a = [1,2,3,4,4,4,5,8,8,6,6,3,3,4,4]

def remove_duplicate(my_list):
	## To make a copy of the my_list , otherwise it will mutate the original list
	new_list = list(my_list)
	one_more = [new_list.pop(0)]
	for element in new_list:
		if int(one_more[-1]) != int(element):
			one_more.append(element)
	print one_more
	return one_more

remove_duplicate(a)	

b = lambda x, y: x * y

print b(10,15)

		