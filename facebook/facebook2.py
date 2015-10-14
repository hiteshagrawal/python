#!/usr/bin/python
import math
file1 = open("dataset1.csv",'r')
file2 = open("dataset2.csv",'r')
my_animal = {}
for line in file2:
	if line.find('bipedal') != -1:
		line = line.strip()
		words = line.split(",")
		my_animal[words[0]] = words[1]  ## We are saving stride length here.
file2.close()
		
#print my_animal

my_dict = {}
for line2 in file1:
	line2 = line2.strip()
	words2 = line2.split(",")
	my_dict[words2[0]] = words2[1]  ## We are saving leg length here.
file1.close()
print my_dict
## Now create a dictionaries which contains both the stride length and leg length
new_dict = 	{}
for animal in my_animal.keys():
	my_animal[animal] = [my_animal.get(animal) , my_dict.get(animal) ]  ## We are saving stride and leg length here

## Now calculate speed
#speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#Where g = 9.8 m/s^2 (gravitational constant)	
final_list = []
for key,value in my_animal.items():
	STRIDE_LENGTH = float(value[0])
	LEG_LENGTH = float(value[1])
	speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * 9.8) 
#	print speed
	final_list.append([speed,key])

final_list.sort(reverse=True)
for speed,animal in final_list:
	print "Animal %s having speed %s m/s^2" %(animal,speed) 
	#print sorted((v,k) for k,v in final_list)






