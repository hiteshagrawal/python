#!/usr/bin/python
#The football.csv contains only 1 line and hence we cannot remove the Team line , with cr return
fh = open('football.csv','r')
words3 = []
diff_score = None
for line in fh:
	print line.__repr__()
	a = list(line.split('\r'))
	for i in a:
		words = i.split(',')
		if not words[0] == 'Team':  
			diff_score = int(words[5]) - int(words[6])
			if diff_score < 0:   #We need to convert the minus goals to plus values too
				diff_score = diff_score * -1
        		#print diff_score
        	words3.append([diff_score,words[0]])
        		# my_dict[words[0]] = [words[5],words[6],diff_score]

     		

#print my_dict
#del my_dict['Team']
words3.pop(0)  ## Removing the line with Team
words3.sort()
print " The lowest difference team is %s with the goal difference of %d" %(words3[0][1],words3[0][0])  

for i in range(len(words3)):
	print " The team is %s with the goal difference of %d" %(words3[i][1],words3[i][0])

