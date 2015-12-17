#!/usr/bin/python
## http://people.rit.edu/blbgse/pythonNotes/os.html
## Change all the filenames and directories from upper to lower
"""Hiteshs-MacBook-Air:python hitesha$ ./upper-lower-dir-files.py 
Enter Directory Path: /tmp/NARESH
Renaming file mv /tmp/NARESH/ANCHAL/AVNI/A /tmp/NARESH/ANCHAL/AVNI/a
Renaming file mv /tmp/NARESH/ANCHAL/AVNI/B /tmp/NARESH/ANCHAL/AVNI/b
Renaming file mv /tmp/NARESH/ANCHAL/AVNI/C /tmp/NARESH/ANCHAL/AVNI/c
Renaming file mv /tmp/NARESH/ANCHAL/AVNI/D /tmp/NARESH/ANCHAL/AVNI/d
Renaming Directory mv /tmp/NARESH/ANCHAL/AVNI /tmp/NARESH/ANCHAL/avni
Renaming file mv /tmp/NARESH/ANCHAL/YASHVI/B /tmp/NARESH/ANCHAL/YASHVI/b
Renaming file mv /tmp/NARESH/ANCHAL/YASHVI/C /tmp/NARESH/ANCHAL/YASHVI/c
Renaming file mv /tmp/NARESH/ANCHAL/YASHVI/D /tmp/NARESH/ANCHAL/YASHVI/d
Renaming Directory mv /tmp/NARESH/ANCHAL/YASHVI /tmp/NARESH/ANCHAL/yashvi
Renaming file mv /tmp/NARESH/ANCHAL/A /tmp/NARESH/ANCHAL/a
Renaming file mv /tmp/NARESH/ANCHAL/E /tmp/NARESH/ANCHAL/e
Renaming file mv /tmp/NARESH/ANCHAL/F /tmp/NARESH/ANCHAL/f
Renaming file mv /tmp/NARESH/ANCHAL/G /tmp/NARESH/ANCHAL/g
Renaming Directory mv /tmp/NARESH/ANCHAL /tmp/NARESH/anchal
Renaming file mv /tmp/NARESH/SURESH/NARESH/B /tmp/NARESH/SURESH/NARESH/b
Renaming Directory mv /tmp/NARESH/SURESH/NARESH /tmp/NARESH/SURESH/naresh
Renaming file mv /tmp/NARESH/SURESH/A /tmp/NARESH/SURESH/a
Renaming Directory mv /tmp/NARESH/SURESH /tmp/NARESH/suresh
Renaming Directory mv /tmp/NARESH /tmp/naresh
Hiteshs-MacBook-Air:python hitesha$ 
"""
import os
fullpath = raw_input("Enter Directory Path: ")
for dirpath, dirs, files in os.walk(fullpath,topdown=False,followlinks=False):
	## First rename files in the last directory from uppercase to lowercase
	for filename in files:
		#print os.path.join(dirpath,filename)
		cmd = 'mv ' + os.path.join(dirpath,filename) + ' ' + os.path.join(dirpath) + '/' + os.path.join(filename).lower()
		print "Renaming file " + cmd
		os.system(cmd)
	#After files, rename the directory from uppercase to lower case	
	#print dirpath	
	cmd = 'mv ' + os.path.join(dirpath) + ' ' + os.path.split(dirpath)[0] + '/' + os.path.basename(dirpath).lower()
	print "Renaming Directory " + cmd
	os.system(cmd)
