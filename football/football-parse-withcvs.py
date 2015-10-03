#!/usr/bin/python

import csv
words = []
with open('football.csv', 'rU') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		if 'Team' not in row:
			#print row
			diff_score = int(row[5]) - int(row[6])
			#print diff_score
			if diff_score < 0:
				diff_score = diff_score * -1
			words.append([diff_score, row[0] ])	
#Now sort the words file with difference score
words.sort()
#print words
print " The lowest difference team is %s with the goal difference of %d" %(words[0][1],words[0][0]) 

for i in range(len(words)):
	print " The team is %s with the goal difference of %d" %(words[i][1],words[i][0])			

