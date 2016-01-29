#!/usr/bin/python

"""https://www.youtube.com/watch?v=Wb-K40mkhEU
https://github.com/jakecoffman/flask-tutorial
"""
import flask, flask.views, os, random
app = flask.Flask(__name__)
## Should be random
app.secret_key = random.random()

class View(flask.views.MethodView):
	def get(self):
		#return "Hello world!"
		return flask.render_template('index.html')

	def post(self):
		#return str(flask.request.form['expression']) ## To return whatever you submit
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return self.get()
		#return "Works!"	

app.add_url_rule('/', view_func=View.as_view('main'), methods = ['GET', 'POST'])		

app.debug = True
app.run()		