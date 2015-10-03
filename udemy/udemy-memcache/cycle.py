

# def cycle(iterable):
# # cycle('ABCD') --> A B C D A B C D
# 	saved = []
# 	print "I am here"
# 	for element in iterable:
# 		yield element
# 		saved.append(element)
# 		print element
# 	while saved:
# 		for element in saved:
# 			yield element


import itertools
SERVERS = ['APP1', 'APP2', 'APP3', 'APP4']
##Infinite Loop Iterator
cycle = itertools.cycle(SERVERS)
def get_server():
	global cycle
	return cycle.next()


for i in range(6):
	print get_server()

print SERVERS
print "starting the best function for iteration"
def get_server():
	try:
		return next(get_server.s)
	except StopIteration:
		get_server.s= iter(SERVERS)
		return next(get_server.s)

setattr(get_server, 's', iter(SERVERS))			

for i in range(7):
	print get_server()

print SERVERS	