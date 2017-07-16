#!/usr/bin/python
"""8.4 Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() function. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt"""
my_list = list()
with open('romeo.txt') as f:
	for line in f:
		line = line.lower().strip().split()
		for word in line:
			if word not in my_list:
				my_list.append(word)

print sorted(my_list)
