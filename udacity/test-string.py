#!/usr/bin/python
def process_madlib(test_string_1):
	#pass
	len_string = len(test_string_1)
	count = -1
	for i in test_string_1:
		count += 1
		if i == 'N':
			#Check if the next 4 characters are noun
			if test_string_1[count:count+4] == 'NOUN':
				print "found a match at pos", count
				print test_string_1[0:count] + "WORD" + test_string_1[count+4:len_string]
				process_string = test_string_1[0:count] + "WORD" + test_string_1[count+4:len_string]
	print process_string			
	count = -1
	for i in process_string:
		count += 1
		if i == 'V':
			if process_string[count:count+4] == 'VERB':
				print "found a match at pos", count
				print process_string[0:count] + "STUD" + process_string[count+4:len_string]
				print process_string[0:count] + "STUD" + process_string[count+4:len_string]


test_string_1 = "This is a good NOUN to use when you VERB your food"
process_madlib(test_string_1)



