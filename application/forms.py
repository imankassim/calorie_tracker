from application import app, db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField


##maybe this should go in create.py/forms.py???
class NewUserForm(FlaskForm):
    first_name = StringField("First Name")
    surname = StringField("Surname")
    kcalneeded = IntegerField("Calories Needed")
    submit = SubmitField("Submit Details")


class NewMealForm(FlaskForm):
    mealname = StringField("Enter the name of your meal")
    kcal = IntegerField("Calories in the meal")
    userid = IntegerField("What is your User ID?")
    submit = SubmitField("Submit Details")

class Login(FlaskForm):
    chosenid = IntegerField("Enter your ID")
    first_name = StringField("First Name")
    surname = StringField("Surname")
    submit = SubmitField("Submit Details")