#!/usr/bin/python
import csv, pandas
from collections import Counter
#fh = open('food.csv','r')
with open('food.csv','r') as fh:
	records = list(csv.DictReader(fh))
	print type(records)
	print len(records)
#fh.close()

## Find out the number of restaurant which passed ,failed the food test
passed = [pass1 for pass1 in records if pass1['Results'] == 'Pass']
failed = [fail for fail in records if fail['Results'] == 'Fail']

print len(passed)
print len(failed)

dba = Counter()
for f in records:
	if f['Results'] == 'Fail':
		dba[f['DBA Name']] += 1

## Print the most common top 10 restaurants which have failed the inspection
print dba.most_common(10)

### get the voilations details
voilations = [x['Violations'] for x in records if x['Results'] == 'Fail']
print voilations[1]
each_voilation = []
voilation_number = {}
voilation_def = {}
## Each voilation is now split with a pipe |
for x in voilations:
	if x is not '':
		each_voilation += x.split("|")
		for y in x.split("|"): ## Set the first number  before . as voliation number
			voilation_number[int(y.split('.')[0])] = voilation_number.get(int(y.split('.')[0]),0) + 1 
			#voilation_number[y.split('.')[0]] = [voilation_number.get(y.split('.')[0][0],0) + 1 , y.split('.')[1] ]
			voilation_def[int(y.split('.')[0])] = voilation_number.get(y.split('.')[1],'') or y.split('.')[1] 

# print len(each_voilation)
# print len(voilation_number)
# print voilation_number
# print len(voilation_def)
# print voilation_def['24']

## Now combine voilation number with occurance and voilation defination
for keys in voilation_number.keys():
	voilation_number[keys] = [ voilation_number[keys], voilation_def[keys] ]

#print voilation_number['24']	
# print "Test"
# print type(each_voilation)
# print each_voilation[3]


#ab = Counter(each_voilation)

#print ab.most_common(10)
### get the lease common
#print ab.most_common()[-1]
# for r in each_voilation:
# 	ab[r.split['.'][0]] += 1

# type(ab)	

voliation_type = Counter(voilation_number)
## Top Three common voilation , with voilation_number = [ occurence , defination ]
print "Top Three common voilation"
for i in voliation_type.most_common(3):
	print i

## least 3 common voilation , with voilation_number = [ occurence , defination ]
print "Least 3 common voilation"
for i in voliation_type.most_common()[:-4:-1]:
	print i