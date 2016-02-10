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
a = [3, 1, 4, 5, 19, 6, 8]
b = [14, 9, 22, 36, 8, 0, 64, 25]
for i in b:
	i_sq = i ** 0.5  ## Getting the square root
	## Now check the decimal values and if that is zero
	deci = int(str(i_sq).split(".")[1])
	sq_root = int(str(i_sq).split(".")[0])
	if deci == 0:
		##Return the number from the original list
		if sq_root in a:
			#print sq_root , i
			print i

