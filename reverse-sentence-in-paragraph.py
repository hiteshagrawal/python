#!/usr/bin/python
import re
def reverse_sentence():
	lines_words = []
	file = raw_input("Enter a file to reverse paragraph: ")
	# try:
	fh = open(file,'r')
	for lines in fh:
		lines = lines.strip()
		sentence = lines.split('.')  ## Each sentence on the line would be an element in the list
		b = ""
		for i in range(len(sentence)):  ## 
			a = str(sentence[i]).split()  ## Now take each sentence , convert it again into string and split them further into words.
			a.reverse()   # Now reversing the elements in each sentence
			b = b + "." + " ".join(a) #  Now creating a string for multiple sentences
		print re.sub('.$', '',b)	## Now removing the full stop from the end of the sentence
	
	fh.close()


reverse_sentence()