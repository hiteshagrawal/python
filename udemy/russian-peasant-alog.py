#!/usr/bin/python
# Russian peasant's algo

# Requirement multiply by small number 2 , divide by 2 , large number , remove the even from the list and then add

# 24 x 16 = ?
#x 12  32
#x 6   64
#3    128
#1    256
#===========
#    256 + 128 = 384

def russian(a,b):
  if a > b:
      large = a
      small = b
  else:
      large = b
      small = a

 # my_tuple = (large, small)
  my_list = []

#my_set.add(my_tuple)
  
  while large/2 >= 1:
      large = large / 2
      small = small * 2
      my_list.append([large,small])
#      print my_list
#Now check for tuple in my_set and if they are even , remove them from the tuple
  new_list = list(my_list)
  for large,small in new_list:
    if (float(large) % 2 == 0.0):
        my_list.remove([large,small])
  z = 0
  for large,small in my_list:
    z += small
  print z    

#You need to have one number as even, if both are odd this algo will fail
russian(24,16)

russian(238,13) 

russian(192,13)

