#!/usr/bin/python
""" My input is 2234,2234,765,2,3,44,44,55,33,33,2,33,33,33
my o/p 
2234:2,765,2,3,44:2,55,33:2,2,33:3"""

my_input = "2234,2234,765,2,3,44,44,55,33,33,2,33,33,33,1"

#def parse(my_input)
my_list = my_input.split(",")
#print my_list
initial = my_list.pop(0)
counter = 1
my_str = ""
for number in my_list:
	#print number
	if initial == number:
		counter += 1
		#print initial
		#print counter
	else:	
		my_str = my_str + ",%s:%s" %(initial,counter)
		counter = 1
	initial = number
my_str = my_str + ",%s:%s" %(initial,counter)	

print my_str[1:].replace(":1","")
