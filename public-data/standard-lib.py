#!/usr/bin/python
import csv
fh = open("potholes.csv")
records = csv.DictReader(fh) ## Can iterate only once
## Collecting Address
#addrs = [r'STREET ADDRESS' for r in records]

## Check for completed records
filled = [r for r in records if r['STATUS'] == 'Open']
#print filled
#print len(addrs)
print len(filled)
fh.close()

fh = open("potholes.csv")
potholes = list(csv.DictReader(fh))  ## this will give a each record as a dictionary at each element on the list
fh.close()
print potholes[1]
#print len(potholes)
clark_potholes = [hole for hole in potholes if 'CLARK' in hole['STREET ADDRESS']]
#print len(clark_potholes)
print clark_potholes[1]

addrs = [hole['STREET ADDRESS'] for hole in clark_potholes]
print len(addrs)
print addrs

holes_in_clark = [hole['NUMBER OF POTHOLES FILLED ON BLOCK'] \
                    for hole in clark_potholes if hole['NUMBER OF POTHOLES FILLED ON BLOCK'].isdigit()]
print holes_in_clark
#holes_in_clark = sum[int(hole['NUMBER OF POTHOLES FILLED ON BLOCK']) for hole in clark_potholes if hole['NUMBER OF POTHOLES FILLED ON BLOCK'].isdigit()]

print "Total Number of holes in clark street is : %d" %(sum(int(x) for x in holes_in_clark))

## Collections module
from collections import Counter
words = ['yes', 'but', 'no', 'but', 'yes']
wordcounts = Counter(words)
print wordcounts.most_common()

addrs = [hole['STREET ADDRESS'] for hole in potholes]
print addrs[:10]
tab = Counter(addrs)
print tab.most_common(5)

## Index building using collections -- slide 47
from collections import defaultdict

zip_index = defaultdict(list)
for r in potholes:
	zip_index[r['ZIP']].append(r)

print type(zip_index)
print len(zip_index)
#print zip_index['60640']

##The above can also be achieved without using collections , this is very good , dont forget it hitesh
## using this you can now get all the number of potholes in a particular zipcode.
zip_index1 = {}
for r in potholes:
	zip_index1[r['ZIP']] = zip_index1.get(r['ZIP'], []) + [r]

print type(zip_index1)
print len(zip_index1)
#print zip_index1['60640']

holes_in_60640 = [hole['NUMBER OF POTHOLES FILLED ON BLOCK'] \
                   for hole in zip_index1['60640'] if hole['NUMBER OF POTHOLES FILLED ON BLOCK'].isdigit()]
print "Total Number of holes in zip 60640 is : %d" %(sum(int(x) for x in holes_in_60640))

## Above getting all the holes in zip code 60640

## Pandas library , external library
# import pandas
# potholes = pandas.read_csv('potholes.csv')
# print potholes