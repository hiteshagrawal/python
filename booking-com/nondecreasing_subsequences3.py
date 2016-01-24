#!/usr/bin/python
"""
Problem 1:

Implement a function nondecreasing_subsequences() that, given a sequence of numbers such as:

  [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ]

... will identify and return each contiguous sub-sequence of non-decreasing numbers. E.g. this example input should return this array-of-arrays (e.g. or list-of-lists)

  [ [3,6,61],[6,7,9],[1,7,7],[2,7,7],[2,388],[3,72],[7] ]

(Each array includes a sequence of numbers that do not get smaller. The original order is unchanged.) For a visual example of a non-decreasing, see:
http://en.wikipedia.org/wiki/File:Monotonicity_example1.png

--
"""
a = [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ]
def nondecreasing_subsequences(my_list):
	final_list = []
	initial_element = my_list.pop(0)
	sub_list = [initial_element]  ### Adding first element to our list too
	for element in my_list:
		if element >= initial_element:
			sub_list.append(element)
		else:
			final_list.append(sub_list)
			sub_list = [element] ## Now we are making another list with first element
		initial_element = element	### Changing initial element to subsequent element
	if len(sub_list) > 0:
		final_list.append(sub_list)		
	print final_list	

nondecreasing_subsequences(a)