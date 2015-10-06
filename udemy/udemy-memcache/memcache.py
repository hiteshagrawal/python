

MEMORY = {}

class Memcache:
	def __init__(self):
		global MEMORY
		self.cache = MEMORY
		pass

	def printname(self):
		print str(__name__)

	def set(self, key, value):
		self.cache[key] = value
		return True

	def get(self, key):
		return self.cache.get(key)	

	def delete(self, key):
		if key in self.cache:
			del self.cache[key]

	def flush(self):
		return self.cache.clear()	

	def memory(self):
		return self.cache		


if __name__ == '__main__':
   #printname()
   a = Memcache()
   print type(a) 
   a.set('b', 2)
   a.set('c', 3)
   a.set('d', 4)
   a.set('e', 5)
   a.delete('e')
   print MEMORY
   print a.get('d')
   print a.get('b')
   a.flush()
   print MEMORY