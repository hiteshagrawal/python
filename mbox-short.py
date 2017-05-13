#!/usr/bin/python
email = set()
with open('mbox-short.txt') as fh:
	for line in fh:
		if not line.startswith('From'): continue
		line = line.strip()
		startpos = line.find(' ')
		endpos = line[startpos+1:].find(' ')
		if endpos == -1 :
			endpos = len(line) + 1
		else:
			endpos = startpos + endpos + 1	
		email.add(line[startpos+1:endpos])

print email
		
		
	#print email

with open('mbox-short.txt') as fh:
	for line in fh:
		if not line.startswith('From'): continue
		email = line.strip().split()[1]
		print email
