#!/usr/bin/python
import paramiko
import time
import re
import select
serverlist = []
user   = 'hitesha'
passwd = '#######'
## Read the file which contains hostname
file = raw_input("Enter the file containing servernames on each line:\n")
with open(file) as fh:
	#Remove blanklines and lines that start with #
	for server in fh:
		#if (server.startswith('#') != -1 ) or not re.findall('.', server)  : continue
		if server in ['\n', '\r\n'] or re.findall('^#' , server) : continue
		serverlist.append(server.strip())

print serverlist	

#	try:
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for server in serverlist:
	ssh.connect(server, username=user, password=passwd, look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command("uname -n;date;uptime;cat ~/git/python/test.txt")
	#sleep 2 secs
	# time.sleep(2)
	output = stdout.read()
	print output
	ssh.close()