#!/usr/bin/python

"""Closures

In Python: Wrap functions with functions. Outer functions have free variables that are bound to inner functions.
(i.e attached data to inner functions)

Useful as function generators

>>> def add_x(x):
...     def adder(num):
...             return x + num
...     return adder
...
>>> add_5 = add_x(5)
>>> add_5
<function adder at 0x10ec24230>
>>> add_5(10)
15
>>> add_5(2)
7
>>>

Notice the function attributes

>>> add_5.func_name
'adder'
>>>
"""
def add_x(x):
	def adder(num):
		return x + num
	return adder
	
add_5 = add_x(5)
print add_5
print add_5(10)
print add_5(17)
print add_5.func_name		




 

