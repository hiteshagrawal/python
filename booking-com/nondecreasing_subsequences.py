#!/usr/bin/python
"""Problem 1:
 
Implement a function nondecreasing_subsequences() that, given a sequence of numbers such as:
 
  [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ]
 
... will identify and return each contiguous sub-sequence of non-decreasing numbers. E.g. this example input should return this array-of-arrays (e.g. or list-of-lists)
 
  [ [3,6,61],[6,7,9],[1,7,7],[2,7,7],[2,388],[3,72],[7] ]
 
(Each array includes a sequence of numbers that do not get smaller. The original order is unchanged.) For a visual example of a non-decreasing, see:
http://en.wikipedia.org/wiki/File:Monotonicity_example1.png"""

#a = [ 3,6,61,6,7,9,1,7,7,2,7,7,2,388,3,72,7 ]
a = [ 3,6,61,62,6,7,9,1,7,7,2,7,7,2,388,3,72,7,6,8,9,3 ]

def nondecreasing_subsequences(my_list):
	final_list = []
	sub_list = []
	init = my_list.pop(0)
	sub_list = [init]
	for i in my_list:
		if i >= init:
			sub_list.append(i)
		else:
			final_list.append(sub_list)	
			sub_list = [i]
		init = i				
	#final_list.append(init)	
	final_list.append(sub_list)		
	print final_list		


				


nondecreasing_subsequences(a)
