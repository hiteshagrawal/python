#!/usr/bin/python
import os
def rename_files():
	file_names = os.listdir("/Users/hitesha/Downloads/udacity/prank/")
	print file_names
	saved_dir = os.getcwd()
	os.chdir("/Users/hitesha/Downloads/udacity/prank/")
	for file in file_names:
		os.rename(file, file.translate(None,"0123456789"))
	new_names = os.listdir("/Users/hitesha/Downloads/udacity/prank/")
	print new_names	
	os.chdir(saved_dir)


rename_files()

