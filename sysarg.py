#!/usr/bin/python
"""
Hiteshs-MacBook-Air:python hitesha$ ./sysarg.py 1 2 3 4
This is sys.argv[0] ./sysarg.py
This is sys.argv[1] 1
This is sys.argv[2] 2
This is sys.argv[3] 3
This is sys.argv 1 onwards ['1', '2', '3', '4']
This is sys.argv 1 but not including 3 ['1', '2']
This is sys.argv starting from 2 to end ['2', '3', '4']
Only even arguments ['./sysarg.py', '2', '4']
Only odd arguments ['1', '3']
"""

import sys

print "This is sys.argv[0]" , sys.argv[0]
print "This is sys.argv[1]" , sys.argv[1]
print "This is sys.argv[2]" , sys.argv[2]
print "This is sys.argv[3]" , sys.argv[3]
print "This is sys.argv 1 onwards" , sys.argv[1:]
print "This is sys.argv 1 but not including 3" , sys.argv[1:3]
print "This is sys.argv starting from 2 to end" , sys.argv[2:]
print "Only even arguments" , sys.argv[::2]
print "Only odd arguments" , sys.argv[1::2]
print "length of sys.argv" , len(sys.argv)