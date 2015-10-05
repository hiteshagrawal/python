#!/usr/bin/python
import urllib as url
web_data = url.urlopen("https://docs.python.org/2/library/urllib.html") # Returns the file like object
print type(web_data)
print web_data.read()
#print "Hi"
#Downloading files using urllib.urlretrieve  , to download a specify web resource
web_content = url.urlretrieve("https://docs.python.org/2/library/urllib.html", "urllib.html") # this will create a urllib.html in current directory

#print web_content