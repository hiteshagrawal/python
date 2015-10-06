import fake_database

from memcache import Memcache 

CACHE = Memcache()

def printName():
	return str(__name__)

def updateLastMultiplied(a, b, result):
	key = 'lastFive'
	lastFiveList = CACHE.get(key)
	if lastFiveList:
		if len(lastFiveList) >= 5:
			##The list already have five itms in it
			newList = lastFiveList[1:]
			newList.append('{}x{}={}'.format(a,b,result))
			done = CACHE.set(key, newList)
		else:
		## The list had less than five items
			lastFiveList.append('{}x{}={}'.format(a,b,result))
			done = CACHE.set(key, lastFiveList)
	else:
		## The was nota a Cache so create one
		done = CACHE.set(key, ['{}x{}={}'.format(a,b,result)]) 
	#return "Last 5:", CACHE.get(key)			
    
def lastMultipliedHandler():
	key = 'lastFive'
	last = CACHE.get(key)
	if last:
		return "Last 5 = {}".format(last)
	else:
		return "Russian not Used Before"

	

def multiplyHandler(a, b):
	key = (a,b)
	cachedAnswer = CACHE.get(key)
	if cachedAnswer:
		return cachedAnswer
	else:
		result = fake_database.russian(a, b)
		updateLastMultiplied(a,b,result)
		done = CACHE.set(key, result)
		return 'Latest Result: {}'.format(result)
		lastMultipliedHandler()
	


if __name__ == '__main__':
	multiplyHandler(26,13)
	multiplyHandler(5,6)
	multiplyHandler(10,6)
	multiplyHandler(12,6)
	multiplyHandler(24,6)

print CACHE.printname()
