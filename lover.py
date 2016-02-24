from flask import Flask,request,render_template,url_for
from os import listdir
# configuration
USERNAME="wxhmzl"
PASSWORD="512902"
app=Flask(__name__)
app.config.from_object(__name__)
@app.route('/')
def gallery():
	img=[f for f in listdir('static/thumbnail')]
	return render_template('index.html',jimg=img)
@app.route('/map')
def map():
	return render_template('map.html')
@app.route('/getmarkerinfo')
def getmarker():
	return "{location:[123,123]}"
if __name__=='__main__':
	app.run(debug=True)