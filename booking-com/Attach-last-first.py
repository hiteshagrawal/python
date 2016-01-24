#!/usr/bin/python
"""
Given a list/array of names(String) sort them such that each name is 
followed by a name which starts with the last character of the previous name. 
# input 
[ 
Luis 
Hector 
Selena 
Emmanuel 
Amish 
] 

# output: 
[ 
Emmanuel 
Luis 
Selena 
Amish 
Hector 
]
"""
names = [ "Luis", "Hector", "Selena", "Emmanuel", "Amish" ]

firsts = {}
lasts = {}

for i in names:
        lasts[i[-1]] = i;

for i in names:
        firsts[i[0].lower()] = i;

print firsts
print lasts       

print set(firsts.keys())
print set(lasts.keys())

start = list(set(firsts.keys()) - set(lasts.keys()))[0]; ## This will return e

print set(firsts.keys()) - set(lasts.keys())
print start

i = 0;
while i < len(names):
        if i == 0:
                print firsts[start]; ## This will print Emmanuel
                last = firsts[start][-1]; ## Taking the last character of the first word , which is l, so last=l
                i = i + 1;
                continue

        print firsts[last];  ## This will print Luis
        last = firsts[last][-1]; ### This will get s from the luis  , last value will be s
        i = i + 1;