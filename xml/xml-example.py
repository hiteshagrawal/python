#!/usr/bin/python
#https://docs.python.org/2/library/xml.etree.elementtree.html
import urllib as url
import xml.etree.ElementTree as et

web_data = url.urlopen("http://www.w3schools.com/xml/cd_catalog.xml")
str_data = web_data.read()  ## To conver web data into string and print it out
#print str_data
#Save the xml file
save_data = url.urlretrieve("http://www.w3schools.com/xml/cd_catalog.xml","cd_catalog.xml")

# Create xml data object
#tree = et.fromstring(str_data)  ## To parse the xml data from string
tree = et.parse('cd_catalog.xml')
xml_root = tree.getroot()
#print xml_root.tag
#print xml_root.attrib
#print xml_root[0][4].text

#cd_list =  xml_root.findall("CD")

# for cd_list in xml_root.findall("CD"):
# 	price = cd_list.find('PRICE').text
# 	title = cd_list.find('TITLE').text
# 	print title, price

#Now list the titles whose price is more than $10
for cd_list in xml_root.findall("CD"):
	price = cd_list.find('PRICE').text
	title = cd_list.find('TITLE').text
	if float(price) > 10:
		print title, price

for price in xml_root.iter('PRICE'):
	#old_price = price.find("PRICE").text
	new_price = float(price.text) * 1.1  ## Increase the price by 10%
	price.text = str(new_price)
	#price.set('updated','yes')
	tree.write('newoutput.xml')  # Write the file with increase prices



