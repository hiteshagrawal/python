#!/usr/bin/python

#!/usr/bin/python

import socket
#Open socket at my end
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## Now connect to remote host
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	#print type(data)
	if ( len(data) < 1 ) :
		break
	print data
mysock.close()		