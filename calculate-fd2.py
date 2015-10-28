#!/usr/bin/python
#Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016931075186   a  b			INR	1,00,000 Cr.	2.47 %	2,102.24 Cr.	03-12-2015 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016914131994	Fixed Deposit		INR	8,10,374.00 Cr.	8.75 %	8,44,513.00 Cr.	24-03-2016 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913006098	Fixed Deposit		INR	11,54,793.00 Cr.	8.75 %	12,06,355.00 Cr.	02-04-2016 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913003882	Fixed Deposit		INR	5,33,795.00 Cr.	8.75 %	5,48,474.00 Cr.	23-01-2016 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913002933	Fixed Deposit		INR	3,77,528.00 Cr.	9.00 %	3,84,938.00 Cr.	20-12-2015 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913002562	Fixed Deposit		INR	2,16,532.00 Cr.	9.00 %	2,19,964.00 Cr.	05-12-2015 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913002554	Fixed Deposit		INR	2,16,532.00 Cr.	9.00 %	2,19,964.00 Cr.	05-12-2015 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913002556	Fixed Deposit		INR	2,16,532.00 Cr.	9.00 %	2,19,964.00 Cr.	05-12-2015 00:00:00		01-10-2015 15:05:42
# Account Number	Account Type		Currency	Balance	Interest Rate (%)	Maturity Amount	Maturity Date		Status As Of
# 016913002555	Fixed Deposit		INR	2,16,532.00 Cr.	9.00 %	2,19,964.00 Cr.	05-12-2015 00:00:00		01-10-2015 15:05:42
#
import re, gc
# the re.findall gives us a "LIST" of all the numbers something like 1,00,000 followed by 8,10,374 etc.
# Now we again use the string replace method to replace all the "," with "" and then apply int to covert all of them into integers

total = sum([ int(x.replace(',', '')) for x in re.findall('INR\s([0-9]+,?[0-9]+,?[0-9]+)\s*', open('data.txt').read()) ])
print "The total sum of FD is Rs.%i" %(total)
gc.collect()