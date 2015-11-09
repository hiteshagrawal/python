#!/usr/bin/python

def check_sticker(string, sticker):
	original_sticker_list = list(sticker)
	sticker_list = list(sticker)
	sticker_count = 1
	for i in string:
		if i in sticker_list:
			sticker_list.remove(i)
		else:
			sticker_list = sticker_list + original_sticker_list
			sticker_list.remove(i)
			sticker_count += 1

	print "Total Sticker required is: %d "	%(sticker_count)	


my_string = 'hittttttteesh'
my_sticker = 'hitesh'

check_sticker(my_string,my_sticker)
 
