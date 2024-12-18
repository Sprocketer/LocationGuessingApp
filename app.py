from flask import Flask, redirect, render_template, request, session, url_for
import requests
import sqlite3
import json
import random

app = Flask(__name__)

def create():
	with sqlite3.connect('login.db') as db:
		cursor = db.cursor()
		cursor.execute(	"""	CREATE TABLE IF NOT EXISTS Users(
						Username text,
						Password text,
						Primary Key(Username))
				""")
		db.commit()
	print('CREATE')
create()

@app.route('/')
def login():
	return render_template('index.html')

@app.route('/latlong')
def latlong():
	"""global lat
	global lng """
	lat = request.args.get('lat')
	lng = request.args.get('lng')
	print(lat, lng)
	return lat
def getlatlong():
	global latget
	global lngget
	latget = session.get('latget', None)
	lngget = session.get('lngget', None)
	print(latget)
	return latget


@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/select', methods=['post'])
def select():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (request.form['un'],request.form['pw']))
    match = len(cur.fetchall())
    con.close()
    if match == 0:
        return "wrong username and password"
    else:
        return "welcome " + request.form['un']

@app.route('/insert', methods=['post'])
def insert():
	con = sqlite3.connect("login.db")
	cur = con.cursor()
	cur.execute(""" INSERT INTO users (username, password)
			VALUES (?, ?) """,
			(request.form['un'], request.form['pw']))
	con.commit()
	con.close()
	return 'signup successful'

@app.route('/solo')
def solo():
	base = "https://graph.mapillary.com/images?access_token=MLY|7884436731651628|991d31489dc0ba2a68fd9c321c4d2cd1&fields=id&bbox="
	bbox1 = "-6.3872,50.3966,1.7623,55.8113"
	bbox = "-180,-90,180,90" 
	x = requests.get(base + bbox, params={'limit': 10})
	parsed_data = json.loads(x.text)
	image = parsed_data['data'][0]['id']
	access_token = "MLY|7884436731651628|991d31489dc0ba2a68fd9c321c4d2cd1"
	print(image)
	url = f"https://graph.mapillary.com/{image}?access_token={access_token}&fields=id,computed_geometry,detections.value"
	y = requests.get(url, params={'limit': 1})
	locations = json.loads(y.text)
	print(locations)
	lngget = locations['computed_geometry']['coordinates'][0]
	latget = locations['computed_geometry']['coordinates'][1]
	def sendlatlng():
		session['lngget'] = lngget
		session['latget'] = latget
		return redirect(url_for('latlong'))
	
	
	
	return render_template('solo.html', image=image)

#app.run() 