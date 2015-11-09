#!/usr/bin/python
#Lecture 44 and 45
mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."
import re
#a = re.match(pattern, string, optional flags)
a = re.match("You", mystr)
#re.match("you", mystr, re.I)  ## to ignore case  , to locate the string at start of the string
#
print a.group()
## Will return You

#search()

# a = re.search(pattern, string, optional flags) , will do a extended search
#show ip arp
arp = "22.22.22.1      0   b4:a9:5a:ff:c8:45  VLAN#222		L"

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
## + 1 or more rep  of previous char, * 0 or more rep   , ? zero or one  , ? makes non greedy
##\d - any single digit from 0 to 9
# \s - matches a white space  , or tab etc
#{2,}  , match 2 repetition of two white spaces
#\w  matches any word characters  and _
#()  -- creates  a group  --> a.group(1)
#a.group(0) is the entire line match
print a.group(0)
# a.groups()  , gives a list of tuples
print a.groups() 

## Third  function findall()

## re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
##Above will match  -> ['22.22.22.1']

#Explaination of above
## r -> raw match
## \d will match digit
## \. will match .  
##\d{2} , matches two digit
##[0-9]  , self explaininatory
##[0-9]{1,3} , matches 0 to 9 for maximum 3 times and min 0 times

## Now see how () affects the pattern matching 
## a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)  ## Will do all th matching patterns 
## the above will return following
## [('22', '22', '22', '1')]   --> returns a list of tuple

## re.sub function  , to subsitute the function
# b = re.sub(r"\d", "7" , arp)  ## will replace all the digit by 7 