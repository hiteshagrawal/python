#!/usr/bin/python

def reverse_para():
	lines_words = []
	file = raw_input("Enter a file to reverse paragraph: ")
	try:
		fh = open(file,'r')
		for lines in fh:
			lines = lines.strip()
			lines_words = lines.split()
			#print lines_words
			lines_words.reverse()  ## to reverse each word in the line
			print " ".join(lines_words)
		fh.close()
	except:
		print "You enter a wrong file"
		fh.close()


reverse_para()