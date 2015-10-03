#!/usr/bin/python

file = 'my-data'
#line = ''
words = []
word = []
my_set = set([])
fh = open(file)
for deposit in fh:
	if deposit.startswith('0'): 
		deposit = deposit.strip()
		words = deposit.split()
		word.append([words[0],words[4]])
		my_set.add((words[0],words[4]))  ## You cannot add list to sets , coz list is mutable
#print my_set	
rs = 0
count = 1
for key,value in my_set:
	print count , key, value
	count += 1
	rs += float(value.replace(',',''))
print "Total Rs:", rs		

fh.close()
