from urllib import request

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#https://www.youtube.com/watch?v=qbLc5a9jdXo
#this is a python script to create an API application (ie you are a producer)

#configure data base so it can be connected to. Create a dabase name SQL Lite data.db and place in same directory. This is an object relational mapper
#this crates the SQLAlchemy URI for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#create a class to store drink objects. This uses SQL Alchemy to create a database. Create your database
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable =False)
    description = db.Column(db.String(120))

    #override a method to show the output of your object
    def __repr__(self):
        return f"{self.name} - {self.description}"

#define the index route
@app.route('/')
def index():
    return 'Hello!'

#create an endpoint in the URL
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name':drink.name, 'description': drink.description}

        output.append(drink_data)
    return {"drinks":output}

#create an endpoint with an ID/parameter
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description":drink.description}

#set up a post function
@app.route('/drinks',methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

#delete a drink method
@app.route('drinks/<id>',methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error" : "not found"}
    db.session.delete(drink)
    db.session.commit()
    return{"message": "deleted"}
'''
various steps that need to occur every time you open up a new terminal (prior data is wiped):
1) export FLASK_APP=application.py <<or whatever your file name is for your application
2) export FLASK_ENV=development
3) flask run
4) CTRL+C to quit server
For creating the database
5) python3 << to execute python executable in your venv
6) from application import db << specify that you want to create a database
7) from applicaiton import Drink << anything you want to use in your commands needs to imported
8) db.create_all() << start creation of database
9) drink = Drink(name="Grape Soda", description="Tastes like grapes") <<create a drink opject
10) drink <<checks if you created a drink object
11) db.session.add(drink) << add the drink to the table
12) db.session.commit() << commit the change
10) db.session.add(Drink(name="Cherry", description="Tastes like that one ice cream"))
11) db.session.commit
'''