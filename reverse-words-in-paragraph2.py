#!/usr/bin/python
def word_reverse():
	try:
		with open(raw_input("Enter filename:")) as fh:
			for line in fh:
				line = line.strip().lower()
				words = line.split()
				words = words[::-1]
				#print words
				print " ".join(words)
	except:
		print "Entering exit"
		exit()		

if __name__ == '__main__':
	word_reverse()
