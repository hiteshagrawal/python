#!/usr/bin/python
# Check whether a word and its reverse both are same
# for e.g "madam" = "madam"
# print zero if true and -1 if false
# >>> bool(1)
# True
# >>> bool(0)
# False
# >>> int(True)
# 1
# >>> int(False)
# 0

def check_palindrome(my_word):
	is_palindrome = int(my_word == my_word[::-1]) -1
	print is_palindrome

if __name__ == '__main__':
		check_palindrome("adam")
		check_palindrome("madam")	
