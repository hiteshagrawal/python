#!/usr/bin/python

file = raw_input("Enter file name:")
my_dict = {}
try:
	fh = open(file,'r')
	print type(fh)
	for line in fh:
		line = line.strip().lower()
		words = line.split()
		for word in words:
			if not word.isdigit():
				my_dict[word] = my_dict.get(word,0) + 1
	fh.close()
except:
	print("Your filename {} is not valid").format(file)

#print my_dict	
my_list = []
for k,v in my_dict.items():
	my_list.append((v,k))

my_list = sorted(my_list,reverse=True)
for x in range(10):
	print my_list[x]	

# try:
# 	fh = open(file,'r')
# 	print type(fh)
# except:
# 	print("Your filename {} is not valid").format(file)	