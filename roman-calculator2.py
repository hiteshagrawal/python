#!/usr/bin/python
val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

my_keys = val.keys()
a = 0

while a == 0:
	string = str(raw_input("Enter a Roman string:"))
	for inp in string.upper():
		if inp in my_keys:
			#print inp
			a = 2	
		else:
			a = 0
			print "Enter only Roman strings:"
			break  ## To break out of the for loop

total = 0	
while string:
	if len(string) == 1 or val[string[0]] >= val[string[1]]:
		total += val[string[0]] 
		string = string[1:]
	else:
		total += val[string[1]] - val[string[0]]
		string = string[2:]

print "The numerical value is %d" %(total)		