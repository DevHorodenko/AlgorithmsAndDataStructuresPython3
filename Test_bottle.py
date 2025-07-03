from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>My web page!</h1></center>
<center><p>Python is an easy language to learn, you don't write much and it's very educational. The Python course will give you the foundation you need to program in this fantastic language!<p><center>
<center><a href="/python">Click here to access next page!</a></center>
'''

@app.route('/')
def index():
	return msg

@app.route('/python')
def page1():
	return '<center><h1>Hello World!</h1></center>\
			<center><a href="/">Back to main page!</a></center>'

run(app, host='localhost', port=8080)