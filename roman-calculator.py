#!/usr/bin/python
val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convert_roman():
    a = 0
    while a == 0 :
        string = str(raw_input('Enter a roman numeral: '))
        my_list = val.keys() ## We are taking the keys from the dictionaries
        for alpha in string.upper():
            if alpha in my_list:
                a = 2  ### This will check that input is either of i,v,x,l,c,d or m only
            else:
                a = 0   ### if you enter something else , it will reset the a to 0 and loop again
                break  ## this will break the for loop as soon as we encounter an error input
        continue

    string = string.upper()
    total = 0
    while string:
        if len(string) == 1 or val[string[0]] >= val[string[1]]:
            total += val[string[0]]
            string = string[1:]
        else:
            total += val[string[1]] - val[string[0]]
            string = string[2:]
    print total

convert_roman()