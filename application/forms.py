from application import app, db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


##maybe this should go in create.py/forms.py???
class NewUserForm(FlaskForm):
    first_name = StringField("First Name")
    surname = StringField("Surname")
    kcalneeded = IntegerField("Calories Needed")
    submit = SubmitField("Submit Details")