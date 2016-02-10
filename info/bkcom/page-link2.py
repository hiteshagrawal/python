#!/usr/bin/python
"""Problem 3:

Write a function get_hops_from(page1, page2) that will determine the number of hyperlinks that you would need to click on to get from some page1 on the web to some other page2 on the web.

For example, if each page below links to the pages that are indented below it, e.g. page 1 links to pages 2 and 5, 
and page 2 links to pages 3 and 4, and page 5 links to pages 3 and 7, 
then the get_hops_from(page1, page7) should return 2 (2 hops), 
since you have to hop once from page 1 to 5 and once more from page 5 to page 7.


page1 :       distance == 0
    page2 :   distance == 1
      page3 : distance == 2
      page4 : distance == 2
    page5 :   distance == 2
      page3 : distance == 2
      page7 : distance == 2

Assume that an API is available to:
* get_links(a_page) will return an array/list of all pages that a_page links to
"""
def get_links(page):
    my_dict = {"page1":["page2", "page5"], "page2":["page3","page4"], 
  	"page5":["page3","page7"], "page3":[], "page4":[], 
  	"page6":[], "page7":["page8","page9"], "page8":["page10"], "page9":[]}
    try:
        return my_dict[page] ## This will return an array
    except:
        return []

my_pages = []
def get_hops_from(pg1,pg2,count=0):
    global my_pages
    my_links = get_links(pg1) ### returns a list
    #print my_links
    for pages in my_links:
        if pages == pg2:
            print "Found"
            my_pages.append(pg1)
            count += 1
            print my_pages, ": distance == %d" %(count)
            return
    else:
            get_hops_from(pages,pg2,count + 1)

get_hops_from("page1","page7")
