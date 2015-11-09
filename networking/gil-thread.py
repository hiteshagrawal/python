#!/usr/bin/python
#http://www.dabeaz.com/python/UnderstandingGIL.pdf
from threading import Thread
def countdown(n):
	print "Running with countdown:", str(n)
	a = n
	while n > 0:
		n -= 1
	#s	print "thread:" , str(a) , str(n)
	print "Finished the thread with count:", str(a)

COUNT = 100000000 # 100 million
#countdown(COUNT)	
t1 = Thread(target=countdown,args=(COUNT//2,))
t2 = Thread(target=countdown,args=(COUNT//4,))
t3 = Thread(target=countdown,args=(COUNT//3,))
t4 = Thread(target=countdown,args=(COUNT//5,))
t5 = Thread(target=countdown,args=(COUNT//4,))
t1.start(); t2.start(); t3.start(); t4.start(); t5.start()
t1.join(); t2.join(); t3.join(); t4.join(); t5.join()