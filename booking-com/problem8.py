#!/usr/bin/python
import sys
""" My input is 2234,2234,765,2,3,44,44,55,33,33,2,33,33,33
my o/p 
2234:2,765,2,3,44:2,55,33:2,2,33:3"""
my_input = sys.argv[1]
#my_input = "1,7,2234,2234,765,2,3,44,44,55,33,33,2,33,33,33,33,1"
my_list = my_input.split(",")
my_str = ""
#print my_list
init = my_list[0]
count = 0
final_list = []
for i in my_list:
	if i == init:
		count += 1
	else:
		#print init, count
		my_str = my_str + "," + "%s:%s" %(init,count)
		count = 1
	init = i
#print init, count	
my_str = my_str + "," + "%s:%s" %(init,count)

print my_str.replace(":1","")[1:]

#final_list = zip(my_numbers,my_count)	

#print final_list




