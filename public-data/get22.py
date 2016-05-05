import urllib

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml' , 'wb')
f.write(data)
f.close()

#print data
#http://www.transitchicago.com/developers/

# Parse the 'rt22.xml' file and identify all buses traveling
# northbound of Dave's office

office_lat = 41.980262

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

#print type(doc)

for bus in doc.findall('bus'):
	lat = float(bus.findtext('lat'))
	if lat >= office_lat:
		direction = bus.findtext('d')
		if direction.startswith('North'):
			lon = float(bus.findtext('lon'))
			id = int(bus.findtext('id'))
			print "Route 22, Bus id %d is at %f lat and %f lon" %(id,lat,lon)


###


