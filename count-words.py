#!/usr/bin/python

file = raw_input('Enter a file name:')
if len(file) < 1 : file = 'test.txt'
try:
   open(file)
except:
   print "Not able to open file", file
   exit()

fh = open(file)
data_dict = {}
for line in fh:
   line = line.strip()
   words = line.split()
   for word in words:
        data_dict[word] = data_dict.get(word,0) + 1

print len(data_dict)
print data_dict
my_list = list(data_dict.items())
print my_list
#print len(my_list)
#bigword = None
#bigcount = None
#for word,count in data_dict.items():
#    if word is None or count > bigcount:
#        bigword = word
#        bigcount = count

#print bigword, bigcount
new_list = []
for k,v in my_list:
    new_list.append((v,k))
new_list.sort(reverse=True)

for val,key in new_list[:10]:
    print key, val
