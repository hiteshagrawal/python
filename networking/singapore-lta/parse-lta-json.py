#!/usr/bin/python
''' Singapore LTA Realtime Data parsing'''
import json,urllib2

## Get account key
with open('lta-api-key') as key:
	accountkey = key.read().strip()

baseurl = 'http://datamall2.mytransport.sg/'	
accidentapi = "ltaodataservice/TrafficIncidents?"
#http://www.pythonlearn.com/code/geojson.py
# Check above to pass parameters to the url
req = urllib2.Request(baseurl + accidentapi)
req.add_header('AccountKey', accountkey)
req.add_header('accept', 'application/json') ## This is default no need to add it
resp = urllib2.urlopen(req)
# resp.headers.headers
# ['Cache-Control: no-cache, no-store, max-age=0\r\n', 'Content-Language: en-US\r\n', 
#'Content-Type: application/json;charset=UTF-8\r\n', 'Date: Tue, 18 Jul 2017 13:41:45 GMT\r\n', 
#'Expires: Thu, 01 Jan 1970 00:00:00 GMT\r\n', 'Pragma: no-cache\r\n', '
#Server: Apache-Coyote/1.1\r\n', 'Content-Length: 2304\r\n', 'Connection: Close\r\n']
# >>> 
#>>> resp.headers.getheader('Content-Length')
#'2304'
#>>> 
# resp.getcode()
# 200
content = resp.read().decode()
resp.close()
data = json.loads(content)
print json.dumps(data, indent=4)

#https://github.com/vgm64/gmplot
## sudo pip install gmplot
##import gmplot
# >>> gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0], 16)
# >>> gmap.scatter(latitudes, longitudes,'k', marker=True)
# >>> gmap.draw("mymap.html")

## google maps , use this and see how it works
### https://github.com/googlemaps/google-maps-services-python
###  geo-coding -apikey = XXXXXXXX

#print content
