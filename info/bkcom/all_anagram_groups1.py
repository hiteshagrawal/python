#!/usr/bin/python
"""Problem 2:

Implement a function all_anagram_groups() that, given many input strings, will identify and group words that are anagrams of each other. An anagram is word that is just a re-arrangement of the characters of another word, like "reap" and "pear" and "a per" (whitespace is ignored). But "pear" and "rep" are not, since "rep" does not have an "a". Also, "the" and "thee" are not anagrams, because "the" only has one "e". 

Given this example input:

[ "pear","dirty room","amleth","reap","tinsel","tesla","hamlet","dormitory","listen","silent" ]

The output should be an array-of-arrays (or list-of-lists)
[
  ["pear","reap"],
  ["dirty room","dormitory"],
  ["amleth","hamlet"],
  ["tinsel","listen","silent"],
  ["tesla"]
]


"""
a = [ "pear","dirty room","amleth","reap","tinsel","tesla","hamlet","dormitory","listen","silent" ]
## convert to string and sort
def all_anagram_groups(my_list):
	temp_list = []
	for element in my_list:
		b = sorted(list(element))
		temp_list.append("".join(b).replace(" ",""))
	#print temp_list	
	### Now make a unique set for temp_list
	my_set = set(temp_list)
	final_list = []
	sub_list = []
	for x in my_set:
		for index,element in enumerate(temp_list):
			if x == element:
				sub_list.append(my_list[index])
		final_list.append(sub_list)
		sub_list = []
	print final_list

all_anagram_groups(a)








def all_anagram_groups(my_list):
	pass
