#!/usr/bin/python
##  Lecture 6
##: AKA - Mediation and DUplication
##:
##: Inouts -> two numbers
#Output - > the solution to those two numbers
# multiplied together using the Russian Peason
# 192 x 13 = 2496
def russian(a,b):
    x = a; y = b                           ## Semicolon -> Compund Statement
    z = 0                                  ## Acumulator 
    print "***********Hit DB*****************"
    print "/////////////////////"
    while x > 0:                           ## While loop Begins
        if x % 2 == 1: z = z + y           ## Modulo Operator
        y = y << 1                         ## Shift Binary over to left , divide by 2 
        x = x >> 1                         ## Shift Binary over to right , multiply by two
    return z

if __name__ == '__main__':
	print russian(192,13)
#2496

# 17 in base 2:    10001 = 17           10001
#                  >> 1                  << 1
#                  1000 = 8             100010 = 34           
