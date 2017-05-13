#!/usr/bin/python

my_dict = {}
with open("test.txt",'r') as fh:
	for line in fh:
		words = line.strip().lower().split()
		for word in words:
			my_dict[word] = my_dict.get(word,0) + 1

my_list = []
for word,count in my_dict.items():
	my_list.append([count,word])

my_list = sorted(my_list,reverse=True)

for i in range(10):
	print("The word \"%s\" appeared \"%d\" times")%(my_list[i][1],my_list[i][0])				