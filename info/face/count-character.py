#!/usr/bin/python
##Count the characters and print the character which is appearing largest time
fh = open("text.txt")

my_file = fh.read()
print my_file
my_dict = {}
for char in my_file:
	if char != ' ' and char != '\n':
		my_dict[char] = my_dict.get(char,0) + 1
fh.close()
print my_dict
my_list = list(my_dict.items())	
print my_list
new_list = []
for char,count in my_list:
	new_list.append((count,char))

new_list.sort(reverse=True)
for count,char in new_list:
	print "The character \'%s\' appeared %d times" %(char,count)