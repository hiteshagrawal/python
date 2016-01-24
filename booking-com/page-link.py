#!/usr/bin/python
"""
Problem 3:

Write a function get_hops_from(page1, page2) that will determine the number of hyperlinks 
that you would need to click on to get from some page1 on the web to some other page2 on the web.

For example, if each page below links to the pages that are indented below it, e.g. page 1 links to pages 2 and 5, and page 2 links to pages 3 and 4, 
and page 5 links to pages 3 and 7, then the get_hops_from(page1, page7) should return 2 (2 hops), since you have to hop once from page 1 to 5 and once more from page 5 to page 7.


page1 :       distance == 0
    page2 :   distance == 1
      page3 : distance == 2
      page4 : distance == 2
    page5 :   distance == 1
      page3 : distance == 2
      page7 : distance == 2

Assume that an API is available to:
* get_links(a_page) will return an array/list of all pages that a_page links to
"""


def get_links(page):
	my_dict = {"page1":["page2", "page5"], "page2":["page3","page4"], "page5":["page3","page7"], "page3":[], "page4":[], "page6":[], "page7":{"page8","page9"}, "page8":["page10"]}
	return my_dict[page] ## This will return an array

def get_hops_from(page1, page2, counter = 0):
	counter = counter
	data = get_links(page1) ## This is a array
	if page2 in data:
		print counter + 1
		return True
	else:
		for new_page in data:
			if get_hops_from(new_page, page2, counter + 1):
				break
	#print counter
my_pages = []
def get_hops_from(page1, page2, counter = 0):
	counter = counter
	data = get_links(page1) ## This is a array
	if page2 in data:
		my_pages.append(page1)
		print "To reach %s from %s" %(page2,my_pages[0])
		print my_pages, "no of links required:", counter + 1
		return True
	else:
		for new_page in data:
			if get_hops_from(new_page, page2, counter + 1):
				break			

get_hops_from("page1","page2")
get_hops_from("page1","page7")
get_hops_from("page1","page9")
#get_hops_from("page2","page9")
