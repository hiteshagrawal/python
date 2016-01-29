#!/usr/bin/python
## Run it with a file as a parameter
"""
Hiteshs-MacBook-Air:booking-com hitesha$ ./problem9.py input 
6 - one (times: 1) 
5 - two (times: 2) 
4 - four (times: 3) 
3 - three (times: 3) 
2 - five (times: 6) 
1 - six (times: 7) 
$ cat input
one two two three three three four four four five five five five five five six six six six six six six

"""
import sys
def word_count():
	#lines_words = []
	new_list = []
	file = sys.argv[1]
	my_dict = {}
#	try:
	fh = open(file,'r')
	for lines in fh:
		#print lines
		lines = lines.strip()
		#lines = lines.lower()
		words = lines.split()
		for word in words:
			my_dict[word] = my_dict.get(word, 0) + 1
	lines_words = list(my_dict.items())
	fh.close() 
	#print my_dict
	for k,v in lines_words:
		new_list.append((v,k))
	#print new_list
	new_list.sort()
	my_rank = len(new_list)
	for i in range(len(new_list)):
		print my_rank, "-" , new_list[i][1] , "(times: %d) " %(new_list[i][0])
		my_rank -= 1

word_count()


