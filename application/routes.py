from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import session
from sqlalchemy.sql import text
from sqlalchemy.sql.type_api import STRINGTYPE
from werkzeug.wrappers import request
from application import app
from flask import render_template, request

dbName = 'testDB.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbName
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)

class patientLogin(db.Model):
        __tablename__ = 'patientLogin'
        id = db.Column('a', primary_key = True)
        usernameDB = db.Column('username', db.String)
        passwordDB = db.Column('password', db.String)
         
    

@app.route("/", methods = ["GET", "POST"])
def getData():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
    
        return username + " " + password
    return render_template("index.html")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
        return render_template("login.html")

