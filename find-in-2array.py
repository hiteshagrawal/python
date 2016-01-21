#!/usr/bin/python
### http://stackoverflow.com/jobs/78567/senior-linux-system-administrator-bookingcom
### http://www.careercup.com/page?pid=bookingcom-interview-questions
## Find a number which exist atleast in two array
## First take all the three arrays and create a set out of it to remove duplicates from within, find out duplicate numbers from that final list

a = [1,2,3,4,4,3,5,6,21]
b = [10,11,2,3,4,10,9,5,10]
c = [11,12,3,4,5,21,31]

## To remove duplicates from each array
set_a = list(set(a))
set_b = list(set(b))
set_c = list(set(c))

# print set_a
# print set_b
# print set_c

final_list = set_a + set_b + set_c

print final_list

## Create a dictionary with count of items
my_dict = {i:final_list.count(i) for i in final_list}
print my_dict
## Now print the numbers which appear more than once
print "Final List"
for num,count in my_dict.items():
	if count > 1:
		print num

#print my_dict
#def find_2(a,b,c):


