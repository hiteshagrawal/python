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

def all_anagram_groups(my_list):
	new_list = []
	final_list = []
	another_list = []
	for word in my_list:
		new_word = "".join(sorted(list(word))).replace(" ","")  ## replace to remove the extra space if any.
		# Better is below , as sorted gives you a sorted array for a string
		#new_word = "".join(sorted(word)).replace(" ","") 
		new_list.append(new_word)  ## We get a new list which is in the same order as the original list but with sorted strings , gr8
		#print new_word
		## Now get the unique items for the new_list
	#print new_list	
	unique_list = set(new_list)
	#print unique_list
	# now loop thru the uniq list set and check at what index it matches in the new_list , take those elements from the original (my_list) list
	temp_list = []
	for elements in unique_list:
		for index,item in enumerate(new_list):
			if item == elements:
				temp_list.append(index)
		#print temp_list		
			## now you have the indexes of duplicate items , which you can fetch from original list
		for index in temp_list:
			another_list.append(my_list[index])
		final_list.append(another_list)
		temp_list = []
		another_list = []	
	print final_list	


all_anagram_groups(a)

### A better solution below with little less mehenath

a = [ "pear","dirty room","amleth","reap","tinsel","tesla","hamlet","dormitory","listen","silent" ]

def all_anagram_groups(my_list):
	new_list = []
	final_list = []
	for word in my_list:
		new_word = "".join(sorted(word)).replace(" ","") ## replace to remove the extra space if any.
		new_list.append(new_word)  ## We get a new list which is in the same order as the original list but with sorted strings , gr8
		#print new_word
		## Now get the unique items for the new_list
	#print new_list	
	unique_set = set(new_list)
	#print unique_list
	# now loop thru the uniq list set and check at what index it matches in the new_list , take those elements from the original (my_list) list
	temp_list = []
	for elements in unique_set:
		for index,item in enumerate(new_list):
			if item == elements:
				temp_list.append(my_list[index])
		final_list.append(temp_list)
		temp_list = []
	print final_list

all_anagram_groups(a)		