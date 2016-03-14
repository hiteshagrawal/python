#!/usr/bin/python



#my_subnet = input("Enter Subnet address:")
my_ip = "192.168.1.100"
my_subnet = "255.255.255.0"

ip = my_ip.split(".")

print ip

# Check the validity of the ip address
while True:
	#my_ip = input("Enter a ip address:")
	if int(ip[0]) <= 223 and (int(ip[1]) != 169 or int(ip[2]) != 254) and (int(ip[1]) <= 254 and int(ip[2]) <= 254 and int(ip[3]) <= 254):
		print "You entered a valid ip"
		break
	else:
		print "You entered a wrong ip"
		continue	  

bin_ip = ""
for a in ip:
	print bin(int(a)).split("b")[1].zfill(8)
	bin_ip += bin(int(a)).split("b")[1].zfill(8)
print bin_ip
print type(bin_ip)	

