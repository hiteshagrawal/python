#!/usr/bin/python

import cherrypy

class FirstPage(object):
	def HandleData(self,data=None):
		return data
	HandleData.exposed = True	
	def index(self):
		#return "<b>Test String<b>"    ## <b> this is the bold html tag
		return """<form action="HandleData" method=post>
				  <input type="text" name="data">
				  <input type="submit" value="Submit!">"""
	index.exposed = True
	
cherrypy.quickstart(FirstPage())		