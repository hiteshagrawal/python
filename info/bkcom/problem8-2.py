#!/usr/bin/python
import sys
""" My input is 2234,2234,765,2,3,44,44,55,33,33,2,33,33,33
my o/p 
2234:2,765,2,3,44:2,55,33:2,2,33:3"""
#my_input = sys.argv[1]
my_input = "1,7,2234,2234,765,2,3,44,44,55,33,33,2,33,33,33,33,1"
my_list = my_input.split(",")
my_str = ""
old = my_list.pop(0)
count = 1
for element in my_list:
	if old == element:
		count += 1
	else:
		my_str += "%s:%d" %(old,count) + ","
		old = element
		count = 1
my_str += "%s:%d" %(old,count)	
print my_str.replace(":1","")		




