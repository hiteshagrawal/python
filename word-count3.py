#!/usr/bin/python

def word_count():
	#lines_words = []
	new_list = []
	file = raw_input("Enter a file to count words: ")
	my_dict = {}
#	try:
	fh = open(file,'r')
	for lines in fh:
		#print lines
		lines = lines.strip()
		lines = lines.lower()
		words = lines.split()
		for word in words:
			my_dict[word] = my_dict.get(word, 0) + 1
	lines_words = list(my_dict.items())
	fh.close() 
	#print my_dict
	for k,v in lines_words:
		new_list.append((v,k))
	#print new_list
	new_list.sort(reverse=True)

	for i in range(10):
		print new_list[i][1] , new_list[i][0]
	# except:
	# 	print "You enter a wrong file"
	# 	fh.close()
	# #Now print the dict	
    

word_count()