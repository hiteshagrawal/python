#!/usr/bin/python
#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
my_list = list()
with open('romeo.txt', 'r') as fh:
	for line in fh:
		words = line.strip().lower().split()
		for word in words:
			if word not in my_list:
				my_list.append(word)

print sorted(my_list)