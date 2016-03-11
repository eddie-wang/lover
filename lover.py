from flask import Flask,request,render_template,url_for,session,redirect
from flask.ext.wtf import Form
from wtforms import PasswordField, SubmitField
from wtforms.validators import Required
from os import listdir,path
import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")
from pymongo import MongoClient
import json
# configuration
USERNAME="wxhmzl"
PASSWORD="512902"

app=Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY']='hard to guess string'
app.debug=True

client= MongoClient('localhost',27017)
db=client.lover

class MyForm(Form):
	password = PasswordField('Password',validators=[Required()])
	submit = SubmitField('Enter')

	def validate(self):
		if not Form.validate(self): return False
		if not self.password.data=="512902": return False
		return True
@app.route('/',methods=['POST','GET'])
def welcome():
	form=MyForm()
	if form.validate_on_submit():
		session['login']=True
		return redirect(url_for('photo'))
	return render_template('welcome.html',form=form)


@app.route('/photo')
def photo():
	if not 'login' in session: return redirect(url_for('welcome'))
	img=[f for f in listdir('/var/www/html/lover/static/thumbnail')]
	return render_template('photo.html',jimg=img)

@app.route('/map')
def map():
	if not 'login' in session: return redirect(url_for('welcome'))
	return render_template('map.html')

@app.route('/time')
def time():
	if not 'login' in session: return redirect(url_for('welcome'))
	return render_template('time.html')
@app.route('/getmarkerinfo')
def getmarker():
	# connect mongodb database
	
	markers=db.marker.find()
	data=[]
	for a in markers:
		a["_id"]=str(a["_id"])
		data.append(a)
	return json.dumps(data)

@app.route('/insertmarker',methods=['POST'])	
def insertmarker():

 	lat=float(request.form['lat'])
	lng=float(request.form['lng'])
	title=request.form['title']
	content=request.form['content']
	img=request.files['img']
	filename=img.filename
	img.save(path.join("static/photo", filename))
	# insert to db
	marker={"location":{"lat":lat,"lng":lng},"title":title,"content":content,"img":filename}
	db.marker.insert_one(marker);
	return "success"

def updatemarker():
	pass

if __name__=='__main__':
	app.run()
