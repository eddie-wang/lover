from flask import Flask,request,render_template,url_for
from os import listdir
import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")
from pymongo import MongoClient
import json
# configuration
USERNAME="wxhmzl"
PASSWORD="512902"
app=Flask(__name__)
app.config.from_object(__name__)
app.debug=True
@app.route('/')
def gallery():
	img=[f for f in listdir('/var/www/html/lover/static/thumbnail')]
	return render_template('index.html',jimg=img)
@app.route('/map')
def map():
	return render_template('map.html')
@app.route('/getmarkerinfo')

def getmarker():
	# connect mongodb database
	client= MongoClient('localhost',27017)
	db=client.lover
	markers=db.marker.find()
	data=[]
	for a in markers:
		a["_id"]=str(a["_id"])
		data.append(a)
	return json.dumps(data)
	
def insertmarker():
	pass

def updatemarker():
	pass

if __name__=='__main__':
	app.run()
