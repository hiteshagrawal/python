#!/usr/bin/python
my_list = []
with open('mbox-short.txt') as fh:
	for line in fh:
		if line.startswith('X-DSPAM-Confidence:'):
			line = line.strip()
			#print line
			stpos = line.find(' ')
			number = line[stpos+1:len(line)]
			my_list += [float(number)]

print my_list
#print sum(my_list)
avg = sum(my_list)/len(my_list)

print("This avg spam confidence is:"),str(avg)