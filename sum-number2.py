#!/usr/bin/python

import re, gc
print sum([int(x) for x in re.findall("[0-9]+", open('sum.txt').read())])
gc.collect()