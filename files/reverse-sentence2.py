#!/usr/bin/python

fh = open('test.txt','r')

for line in fh:
	line = line.strip()   ## This is a string containing each line.
	sentence = line.split(".")  ## Now we will get the sentences from each line as elements in a list
	#print sentence
	b = ""
	for i in range(len(sentence)):
		new_sentence = str(sentence[i]).split()  ## We get the string again but only with 1 sentence
		new_sentence.reverse()  # Now reversing the elements in each sentence
		b = b + "." + " ".join(new_sentence) #  Now creating a string for multiple sentences
	print b

