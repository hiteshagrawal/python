import computer1
import computer2
import computer3


SERVERS = [computer1, computer2, computer3]


def getserver():
	my_server = SERVERS.pop(0)
	SERVERS.append(my_server)
	return my_server

def test_loadbalancer():
	from random import randint
	for i in range(10):
		z = randint(1,21)
		a = [53,44,56,42,55,65,122][z%7]
		b = [44,5,65,122,56,42,57][z%7]
##Run the load balancer algorithm
		server = getserver()
		print server.printName()
		print "{}x{}".format(a,b)
		print server.multiplyHandler(a,b)
		print server.lastMultipliedHandler()
		print " "


if __name__ == '__main__':
#	print getserver()
	test_loadbalancer()

