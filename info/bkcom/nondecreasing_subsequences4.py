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
def nondecreasing_subsequences(my_list):
	final_list = []	
	initial_num = my_list.pop(0) ## To assign the first element in the my_list to initial num
	## Now initial list sublist too with initial element
	sub_list = [initial_num]
	for element in my_list:
		if element >= initial_num:
			sub_list.append(element)
		else:
			final_list.append(sub_list)
			sub_list = [element] ## push the element in a new sub_list
		initial_num = element  ## Now changing the initial number to the next element in the list
	final_list.append(sub_list)  ## This will ensure to push the last list in the final list

	print final_list

def nondecreasing_subsequences(my_list):
	counter = 0
	my_dict = {}
	initial_num = my_list.pop(0)
	my_dict[counter] = [initial_num]
	for i in my_list:
		if my_dict[counter][-1] <= i:
			my_dict[counter] = my_dict.get(counter) + [i]
		else:
			counter += 1
			my_dict[counter] = [i]

	print my_dict.values()		



nondecreasing_subsequences(a)