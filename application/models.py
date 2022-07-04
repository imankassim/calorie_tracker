from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class UserNew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(10), nullable = False)
    sname = db.Column(db.String(10), nullable = False)
    kcalaim = db.Column(db.Integer, nullable = False)
    #DDMMYY
    date = db.Column(db.String(6))
    #nullable = False ^^
    #we need date only regarding meals so not sure?
    meal = db.relationship('Meals', backref = 'usermeal')



class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mealname = db.Column(db.String(50), nullable = False)
    kcal = db.Column(db.Integer, nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey(UserNew.id))