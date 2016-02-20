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
my_dict = {}
## Create a new sorted list
def all_anagram_groups(a):
	for i in a:
		my_string = "".join(sorted(list(i))).replace(" ","")
		#print my_string
		#print type(i)
		my_dict[my_string] = my_dict.get(my_string,[]) + [i] 
		#print my_dict[my_string]
	print list(my_dict.values())	

if __name__ == "__main__":
	all_anagram_groups(a)