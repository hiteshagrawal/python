#!/usr/bin/python
import re
def word_reverse():
	#try:
	with open(raw_input("Enter filename:")) as fh:
		for line in fh:
			line = line.strip().lower()
			sentence = line.split('.')
			#print sentence
			# Now i have to split sentences as well to reverse word inside it
			b = ""
			for i in range(len(sentence)):
				#print sentence[i]
				words = sentence[i].split()  ## Split words in a sentence
				words = words[::-1] ## Reverse the words in a sentence
				b = b + "." + " ".join(words) #  Now creating a string for multiple sentences
		print re.sub('.$', '',b)	## Now removing the full stop from the end of the sentence

	# except:
	# 	print "Entering exit"
	# 	exit()		

if __name__ == '__main__':
	word_reverse()
