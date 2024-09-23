
from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

@app.route('/')
def login():
	return render_template('index.html')

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
