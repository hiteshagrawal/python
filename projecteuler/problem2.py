#!/usr/bin/python
#https://projecteuler.net/problem=2
def fibonacci(number):
	new_num = 2
	old_num = 1
	even_total = 0
	total = 0
	my_array = [old_num,new_num]
	while total < number:
		total = old_num + new_num
		my_array.append(total)
		if new_num % 2 == 0:
			even_total += new_num
		old_num = new_num
		new_num = total	
	print total		
	print my_array
	print "The sum of even fibonacci number till %d is %d" % (number,even_total)


def fibonacci_new(max):
	next = 1
	fibonacci_list = [0]
	while True:
		if next <= max:
			fibonacci_list.append(next)
			next = fibonacci_list[-1] + fibonacci_list[-2]
		else:
			break
	print fibonacci_list			

fibonacci(4000000)



