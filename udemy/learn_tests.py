#!/usr/bin/python
#learn_tests.py

#: testing

#: WHY?
#: To Understand our Code Better.
#: To learn when we made a mistake
#: To know when we are finished
##: To ensure any future programme changes/addition

def adding(a,b):
	return a + b

def test_adding():
	assert adding(3,4) == 7
	assert adding(3,2) != 10
	assert adding(99,49) == 148
	print "All test passed"	

test_adding()	