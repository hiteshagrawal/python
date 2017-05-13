#!/usr/bin/python
my_dict = dict()
with open("test.txt") as fh:
	for lines in fh:
		lines = lines.strip()
		words = lines.lower().split()
		for word in words:
			my_dict[word] = my_dict.get(word,0) + 1

#print my_dict
value = 0
for word,count in my_dict.items():
	if count > value:
		BigCount = count
		BigWord = word
		value = count

print("The word \"%s\" appeared \"%s\" times")%(BigWord,BigCount)		

my_list = list()
for word,count in my_dict.items():
	my_list.append([count,word])

my_list = sorted(my_list,reverse=True)
for i in range(10):
    print my_list[i]
    

