#!/usr/bin/python
def add_10(x):
	"""
	adds 10 to the input
	>>> add_10(5)
	15
	>>> add_10(-5)
	5
	>>> add_10(-2)
	8
	>>> #Comments are ignored
	>>> print "" ## This will pass  , caveat can't print 
	<BLANKLINE>
	>>> "foo" # implicit print
	'foo'
	>>> print "foo"
	foo
	>>> line = "foo\\n"  ## Need to escape backslashes if not using raw
	>>> print line
	foo
	<BLANKLINE>
	"""
	return x + 10

if __name__ == "__main__":
	import doctest
	doctest.testmod()	

""" Try to remove magic numbers , can also be replace by ellipsis "..."
+NORMALIZE_WHITESPACE  ## Dont worry about spacing
+ELLIPSIS, +NORMALIZE_WHITESPACE
SKIP
### printing out dictionary might fail as they are not ordered
dict workaround , sort keys
items = foo.items()
items.sort()
items

Trailing whitespace can bite you , while printing ( make sure you check for spaces)
import doctest
doctest.testfile(filename)  -- to test all the test in filename
 """

def add_x(x):
	def adder(num):
		return x + num
	return adder
 		
add_5 = add_x(5)
add_5
# <function adder at ...>
add_5(10)
# with return 15

call_count = 0
def count(func):
	def wrapper(*args, **kw):
		global call_count
		call_count += 1
		return func(*args, **kw)
	return wrapper	