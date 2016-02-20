#!/usr/bin/python
# coding=utf-8
#https://www.python.org/dev/peps/pep-0263/
"""
$a = [3, 1, 4, 5, 19, 6];
$b = [14, 9, 22, 36, 8, 0, 64, 25];
# Some elements in the second array are squares.  
# Print elements that have a square root existing in the first array.
# $b[1] = 9, it’s square root is 3 ($a[0])  
# $b[3] = 36, it’s square root is 6 ($a[5])  
# $b[7] = 25, it’s square root is 5 ($a[3])   
# Result:  
# 9  
# 36  
# 25
"""
import math
a = [3, 1, 4, 5, 19, 6, 8]
b = [14, 9, 22, 36, 8, 0, 64, 25]
for i in b:
	if math.sqrt(i).is_integer():
		if int(math.sqrt(i)) in a:
			print int(math.sqrt(i))
			## You could have also used set to check for symetric

