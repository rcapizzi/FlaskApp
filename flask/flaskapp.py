from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/hello')
def secondhello():
	return 'This is the second page mate'

