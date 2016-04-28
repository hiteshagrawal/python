#!/usr/bin/python

import re
def open_file(filename):
	try:
		with open(filename,'r') as fh:   ### use with , which will automatically close the file handle in memory after the with block is completed
			print "file open sucessfully"
			# a = fh.read()
			# b = re.findall("[0-9]+", a)
			# print b
			# print type(b[1])
			b = [int(x) for x in re.findall("[0-9]+", fh.read())]
			print type(b)
			print b
			total = sum(b)
			#total = 0
			# for num in re.findall("[0-9]+", fh.read()) :
			# 	total = total + int(num)
			# 	print " " * 32, num.rjust(10)
			# 	# total += int(num)
			# print "============="
			# # print total	
			# # print "============="
			print "The all sum of bla bla lbaTotal:", total

		#fh = open(filename,'r')
	except:
		print "The file you gave doesn't exist", filename
		exit()
	
open_file('sum.txt')				
