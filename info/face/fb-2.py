#!/usr/bin/python

output = []
for i in xrange(1000):
	host =  "web%04d.facebook.com" %(i)
    if ssh(host, "ps aux | grep app | grep -v grep | wc -l ") == 4:
        output.append(host)
return print output        