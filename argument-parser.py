#!/usr/bin/python
#https://docs.python.org/3/library/argparse.html
import argparse
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',const=sum, default=max,
# 					help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args.accumulate(args.integers))

"""Hiteshs-MacBook-Air:python hitesha$ ./argument-parser.py -hl hostlist.txt 
The hostname is None
The filename is hostlist.txt
Hiteshs-MacBook-Air:python hitesha$ ./argument-parser.py -hl hostlist.txt --host myserver
The hostname is myserver
The filename is hostlist.txt
Hiteshs-MacBook-Air:python hitesha$ 
"""

parser = argparse.ArgumentParser(description='Get a hostlist filename')
parser.add_argument('-hl','--hosts',help='File with hostname', required=True)
parser.add_argument('-s','--host',help='Single servername')

args = parser.parse_args()
print("The hostname is {}").format(args.host)
print("The filename is {}").format(args.hosts)
