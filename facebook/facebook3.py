#!/usr/bin/python
# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore

# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal
import math
fh1 = open('dataset1.csv')
fh2 = open('dataset2.csv')
my_animal = {}
for line in fh2:
	if line.find('bipedal') != -1:
		line = line.strip()
		words = line.split(',')
		#STRIDE_LENGTH
		my_animal[words[0]] = [words[1]]

print my_animal

my_dict = {}
for line in fh1:
	line = line.strip()
	words = line.split(',')
	#LEG_LENGTH
	my_dict[words[0]] = [words[1]]

print my_dict
for key in my_animal:
	my_animal[key] = my_animal.get(key) + my_dict[key]

print my_animal
final_list = []
for key,value in my_animal.items():
	STRIDE_LENGTH = float(value[0])
	LEG_LENGTH = float(value[1])
	speed = ((STRIDE_LENGTH  / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * 9.8 )
	final_list.append([speed,key])

final_list.sort(reverse=True)

print final_list	
for speed,animal in final_list:
	print "Animal %s having speed %s m/s^2" %(animal,speed) 
#print sorted((v,k) for k,v in final_list)

fh1.close()
fh2.close()	
