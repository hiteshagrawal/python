#!/usr/bin/python
# Different file modes are read(r), write(w) and append(a)
# While opening file in write mode , if the file exist all the existing data will be overwritten
file_object = open("file1.txt", "w")
phrase = "This will be written to file.\n"
file_object.write(phrase)
file_object.close()

file_object = open("file1.txt", "a")
phrase = "This will be appended to the file.\n"
file_object.write(phrase)
file_object.close()
