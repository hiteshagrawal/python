from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greet/<username>')
def greet(username):
    return 'Hello %s ,how r u today!' %(username)    
#http://127.0.0.1:5000/greet/naresh
#Hello naresh ,how r u today!

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

app.debug = True

if __name__ == '__main__':
    app.run()