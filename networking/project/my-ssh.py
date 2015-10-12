#!/usr/bin/python

import paramiko
import time
import sys
import select

host = '192.168.2.101'
user   = 'teopy'
passwd = 'python'
i = 1

#while True:
#    print "Trying to connect to %s (%i/30)" % (host, i)
#	try:
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=passwd, look_for_keys=False)
# time.sleep(2)
# if ssh.connected() is False:
# 	print "Connection Failed."
# else:
# 	print "Connected to server."
# #		break
# #	except paramiko.AuthenticationException:
# 	    print "Authentication failed when connecting to %s" % host
# 	    sys.exit(1)
# #	except:
# 	    print "Could not SSH to %s, waiting for it to start" % host
# 	    i += 1
# 	    time.sleep(2)

#connection = ssh.invoke_shell()

# Send the command (non-blocking)
stdin, stdout, stderr = ssh.exec_command("show tacacs")  

# Wait for the command to terminate
while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        if len(rl) > 0:
            # Print data from stdout
            print stdout.channel.recv(1024),

# #
# # Disconnect from the host
# #
# print "Command done, closing SSH connection"
ssh.close()
