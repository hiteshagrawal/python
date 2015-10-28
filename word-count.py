#!/usr/bin/python


def word_count():
	my_dict = {}
	file = raw_input("Enter a filename:\n")
	with open(file) as fh:
		for line in fh:
			line = line.strip().lower()
			words = line.split()
			for word in words:
				my_dict[word] = my_dict.get(word,0) + 1
	my_list = []
	for key,value in my_dict.items():
		my_list.append([value,key])
	my_list.sort(reverse=True)
	
	for i in range(10):
		print "The word \"%s\" appeared %s times" %(my_list[i][1],my_list[i][0])

if __name__ == "__main__":		
	word_count()


