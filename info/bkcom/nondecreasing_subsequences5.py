#!/usr/bin/python
"""Problem 1:

Implement a function nondecreasing_subsequences() that, given a sequence of numbers such as:

  [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ]

... will identify and return each contiguous sub-sequence of non-decreasing numbers. E.g. this example input should return this array-of-arrays (e.g. or list-of-lists)

  [ [3,6,61],[6,7,9],[1,7,7],[2,7,7],[2,388],[3,72],[7] ]

(Each array includes a sequence of numbers that do not get smaller. The original order is unchanged.) For a visual example of a non-decreasing, see:
http://en.wikipedia.org/wiki/File:Monotonicity_example1.png
"""

a = [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ]
my_dict = {}

def nondecreasing_subsequences(my_list):
	count = 0
	## Putting the first element in the my_dict at index zero with the list
	my_dict[count] = [my_list.pop(0)]
	#print my_dict , my_dict[count][-1]
	for element in my_list:
		if my_dict[count][-1] <= element:
			## Add the element to the my_dict list
			my_dict[count] = my_dict.get(count,[]) + [element]
		else:
			count += 1	
			my_dict[count] = [element]	
	print my_dict.values()
	return my_dict.values()		

nondecreasing_subsequences(a)