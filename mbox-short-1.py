#!/usr/bin/python
import operator
my_dict = {}
with open('mbox-short.txt') as fh:
	for line in fh:
		if line.startswith('From'):
			line = line.strip().split()
			email = line[1]
			my_dict[email] = my_dict.get(email,0) + 1

# new_list = []
# for key,value in my_dict.items():
# 	new_list.append([value,key])

# new_list.sort(reverse=True)
# for count,email in new_list:
# 	print("Email: %s sent %s emails") %(email,count)

#print my_dict			
# Sort a dictionary on values
sorted_list = sorted(my_dict.iteritems(), key=operator.itemgetter(1), reverse=True)

#print sorted_list
"""[('cwen@iupui.edu', 10), ('david.horwitz@uct.ac.za', 8), 
('zqian@umich.edu', 8), ('louis@media.berkeley.edu', 6), 
('gsilver@umich.edu', 6), 
('rjlowe@iupui.edu', 4), ('stephen.marquard@uct.ac.za', 4), 
('gopal.ramasammycook@gmail.com', 2), ('antranig@caret.cam.ac.uk', 2), 
('wagnermr@iupui.edu', 2), ('ray@media.berkeley.edu', 2)]"""

for email,count in sorted_list:
	print("Email: %s sent %s emails") %(email,count)