from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY' #change to os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

app.static_folder = 'static'

from application import routes