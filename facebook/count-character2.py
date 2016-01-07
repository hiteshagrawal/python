#!/usr/bin/python
##Count the characters and print the character which is appearing largest time
fh = open("text.txt",'r')
my_file = fh.read()
fh.close()
my_dict = {}
for char in my_file:
	if char != ' ' and char != '\n':
		my_dict[char] = my_dict.get(char,0) + 1

print "my_dict", my_dict

my_list = list(my_dict.items())	
print "my_list", my_list
new_list = []
for char,count in my_list:
	new_list.append((count,char))
new_list.sort(reverse=True)
print "new_list", new_list

for count,char in new_list:
	print " The character: %s appears %d times" % (char,count)