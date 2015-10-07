#!/usr/bin/python
# 1. Ask the user for file name
# 2. If file does not exist print 'File cannot be opend please check the file name:', and user input
# 3.if file exists count the number of lines and tell user the count and ask if he still want to open the file
# 4. if user input is y yes Yes or n no No then only open the file in Upper case, else prompt the user that he entered wrong choice.

def cat_file():
	a = 0
	while a == 0:
		file = raw_input("Enter filename to open:\n")
		try:
			#with open(file,'r') as fh:
			fh = open(file,'r')
			a = 2
			break
		except:	
			print "You enter a wrong filename,try again\n"
			continue
	count = 0
	read_data = ""
	#Now count the lines in the file
	for line in fh:
		read_data = read_data + line
		count +=1
	print "The number of lines in the file is", count
	print "Do you still want to open the file and read it"
	user_input = raw_input("Enter [y,yes,n,no]:\n")
	user_input = user_input.lower()
	while a == 2:
		if (user_input == 'y') or (user_input == 'yes'):
			print "Below is the content of file", file
			print read_data.upper()
			a = 0
		elif (user_input == 'n') or (user_input == 'no'):
			print "Exiting"
			a = 0
			fh.close()	
			exit()
		else:
			user_input = raw_input("Enter [y,yes,n,no]:\n")
			user_input = user_input.lower()
			a = 2		
	fh.close()	


cat_file()			