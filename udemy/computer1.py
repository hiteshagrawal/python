import fake_database

CACHE = {}

def printName():
	print str(__name__)

def updateLastMultiplied(a, b, result):
	key = 'lastFive'
	lastFiveList = CACHE.get(key)
	if lastFiveList:
		if len(lastFiveList) >= 5:

			##The list already have five itms in it
			newList = lastFiveList[1:]
			newList.append('{}x{}={}'.format(a,b,result))
			CACHE[key] = newlist
		else:
		## The list had less than five items
			lastFiveList.append('{}x{}={}'.format(a,b,result))
			CACHE[key] = lastFiveList
	else:
		## The was nota a Cache so create one
		CACHE[key] = ['{}x{}={}'.format(a,b,result)]			
    
def lastMultipliedHandler():
	key = 'lastFive'
	if key in CACHE:
		print "Last 5 = {}".format(CACHE[key])
		print "-"*8
		print " "
	else:
		print "Russina not Used"
		print "-"*8
		print " "	
	

def multiplyHandler(a, b):
	key = (a,b)
	if key in CACHE:
		print CACHE[key]
	else:
		result = fake_database.russian(a, b)
		CACHE[key] = result
		lastFiveList.append('{}x{}={}'.format(a,b,result))
		print 'Latest Result: {}'.format(result)
	


if __name__ == '__main__':
	multiplyHandler(2,6)
	multiplyHandler(5,6)
	multiplyHandler(10,6)
	multiplyHandler(12,6)
	multiplyHandler(24,6)

