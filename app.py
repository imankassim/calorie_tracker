from application import app
import os
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

SQLALCHEMY_TRACK_MODIFICATIONS = False
  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
