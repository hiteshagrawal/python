#!/usr/bin/python

a = [ 3,6,61,6,7,9,1,7,7,6,2,7,7,2,388,3,72,7,8 ]

def nondecreasing_subsequences(my_list):
	final_list = []
	init = my_list.pop(0)
	sub_list = [init]
	for element in my_list:
		if element >= init:
			sub_list.append(element)
		else:
			final_list.append(sub_list)
			sub_list = [element]
		init = element
	if len(sub_list) >= 1:
		final_list.append(sub_list)	
	print final_list
	print len(final_list)	

				

def fibonacci(max):
	next = 1
	fibonacci_list = [0]
	while True:
		if next <= max:
			fibonacci_list.append(next)
			next = fibonacci_list[-1] + fibonacci_list[-2]
		else:
			break
	print fibonacci_list			


if __name__ == '__main__':	
	nondecreasing_subsequences(a)
	fibonacci(100)
	fibonacci(1000)