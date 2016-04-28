#!/usr/bin/python
"""Implement a function all_anagram_groups() that, given many input strings, will identify and group words that are anagrams of each other. An anagram is word that is just a re-arrangement of the characters of another word, like "reap" and "pear" and "a per" (whitespace is ignored). But "pear" and "rep" are not, since "rep" does not have an "a". Also, "the" and "thee" are not anagrams, because "the" only has one "e". 

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

def all_anagram(my_list):
	new_dict = {}
	for i in my_list:
		x = i.replace(" ","")
		y = "".join(sorted(list(x)))
		#print y
		new_dict[y] = new_dict.get(y,[]) + [i]
	#print new_dict 
	print new_dict.values()  
	return new_dict.values() 

all_anagram(a)