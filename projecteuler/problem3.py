#!/usr/bin/python
#https://projecteuler.net/problem=3
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
## to check only prime numbers
from datetime import datetime
start=datetime.now()

# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)

def check_prime(n):
	'''check if integer n is a prime'''
    # make sure n is a positive integer
    # 0 and 1 are not primes
	if n < 2:
		return False
	# 2 is the only even prime number	
	if n == 2:
		return True
	# all other even numbers are not primes	
	if not n & 1:
		return False		
	for y in xrange(3,int(n**0.5)+1,2):
		if n % y == 0:
			return False
	return True

def factor_prime(number):
	largest_prime = 0
	for i in xrange(2,number):
		if (number % i) == 0: ## The number is divisible ,  now check whether i is a prime number
			if check_prime(i):
				largest_prime = i
	return largest_prime			


print check_prime(29)
print check_prime(15)
#print check_prime(329875)
#print factor_prime(13195)
#print factor_prime(1319500000)

print factor_prime(600851475143)

print datetime.now()-start