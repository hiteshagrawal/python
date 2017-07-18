#!/usr/bin/python

my_dict = dict()
with open('mbox-short.txt') as fh:
	for line in fh:
		if not line.startswith('From '):
			continue
		line = line.strip().split()
		email = line[1]
		my_dict[email] = my_dict.get(email,0) + 1

print my_dict		

bigemail = None
bigcount = None
for name,count in my_dict.items():
    if bigemail is None or count > bigcount:
        bigemail = name
        bigcount = count

print bigemail, str(bigcount)