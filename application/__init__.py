from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from application.forms import NewUserForm, NewMealForm, Login, CharCheck
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

app=Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY' #change to os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

app.static_folder = 'static'

from application import routes