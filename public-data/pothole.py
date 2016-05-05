#!/usr/bin/python
import csv

fh = open("potholes.csv",'r')
f = csv.DictReader(fh)
potholes_by_address = {}
for row in f:
	address = row['STREET ADDRESS']
	#print address
	## Change address to block
	# >>> addr = '350 N STATE ST'
	# >>> parts = addr.split()
	# >>> parts
	# ['350', 'N', 'STATE', 'ST']
	# >>> num = parts[0]
	# >>> parts[0] = num[:-2] + 'XX'
	# >>> parts
	# ['3XX', 'N', 'STATE', 'ST']
	# >>> " ".join(parts)
	# '3XX N STATE ST'
	# >>>
	if len(address) > 0: ## We don't need empty addresses
		parts = address.split()
		num = parts[0]
		parts[0] = num[:-2] + 'XX'
		address = ' '.join(parts)
		#print address
		no_of_potholes = row['NUMBER OF POTHOLES FILLED ON BLOCK']
		if not str(no_of_potholes).isdigit():
			no_of_potholes = 0
		potholes_by_address[address] = potholes_by_address.get(address,0) + int(no_of_potholes)
		#print potholes_by_address[address]
	
#print len(potholes_by_address)
fh.close()
new_list = [] 		
## now we just need to sort our data:
for key,value in potholes_by_address.items():
	new_list.append((value,key))

new_list.sort(reverse=True)


for potholes,address in new_list[:10]:
	print "Street: %s, No of Potholes: %d" %(address,potholes)


		