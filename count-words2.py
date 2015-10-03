##  Count words

file = raw_input('Enter filename')
try:
    open(file,'r')
except:
    print "Invalid file", file	
    exit()

fh = open(file,'r')
my_dict = {}
for line in fh:
    line = line.strip()
    words = line.lower().split()
    for word in words:
        my_dict[word] = my_dict.get(word,0) + 1

print my_dict