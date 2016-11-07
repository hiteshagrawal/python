#!/usr/bin/python

fh = open('mbox.txt')
print type(fh)
email = []
for line in fh:
	if line.startswith('From '):
		print line.split()[1]
		email.append(line.split()[1])
		
fh.close()	

a = {x:email.count(x) for x in email}
#print a
new_list = []
for k,v in a.items():
	new_list.append([v,k])

print sorted(new_list,reverse=True)	 

for i in sorted(new_list,reverse=True):
	#print "The most number of emails: %s sent by %s" %(i[0],i[1])
	print("The most number of emails: {} sent by {}").format(i[0],i[1])