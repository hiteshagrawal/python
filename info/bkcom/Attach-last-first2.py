#!/usr/bin/python

names = [ "Luis", "Hector", "Selena", "Emmanuel", "Amish" ]

firsts = {}
lasts = {}

for i in names:
	firsts[i[0].lower()] = i
	lasts[i[-1]] = i

print firsts
print lasts

start = list(set(firsts.keys()) - set(lasts.keys()))[0]

print start

i = 0

while i < len(names):
	if i == 0:
		name = firsts[start]
		print name
		last = name[-1]
		i += 1
		continue

	print firsts[last]
	last = firsts[last][-1]
	i += 1		
