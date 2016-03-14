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
a = [ "pear","dirty room","amleth","reap","tinsel","tesla","hamlet","dormitory","listen","silent","top","pot" ]

def all_anagram_groups(my_list):
	#Create a new dict
	my_dict = {}
	for element in my_list:
		a = "".join(sorted(list(element))).replace(" ","")
		my_dict[a] = my_dict.get(a,[]) + [element]
	print my_dict.values()
	return my_dict.values()
	
all_anagram_groups(a)		


