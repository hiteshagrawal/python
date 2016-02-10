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
new_sort_list = []
## Create a new sorted list
def all_anagram_groups(a):
	for i in a:
		new_sort_list.append("".join(sorted(list(i))).replace(" ",""))
	#print "".join(sorted(list("dirty room"))).replace(" ","")
	#print new_sort_list
	uniq_items = set(new_sort_list)
	#print uniq_items
	final_list = []
	sub_list = []
	for element in uniq_items:
		for index,items in enumerate(new_sort_list):
			if element == items:
				sub_list.append(a[index])
		final_list.append(sub_list)
		sub_list = []
	print final_list	

if __name__ == "__main__":
	all_anagram_groups(a)

