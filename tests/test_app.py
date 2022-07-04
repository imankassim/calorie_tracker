from flask import Flask, render_template, request, url_for
from flask_testing import TestCase
from application import app, db
from application.forms import NewUserForm, NewMealForm, Login
from application.models import UserNew, Meals
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired


#imports
from app import app
#from app import app, db



#base class
class TestBase(TestCase):
    def create_app(self):
        #don't need to set as enviroment variable as no need for permanent database while testing
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    #SET UP - RUNS BEFORE TEST
    def setUp(self):
        #create table
        db.create_all()
        #create test entry
        sample1 = UserNew(fname="test", sname="test", kcalaim=8378)
        #save user to db
        db.session.add(sample1)
        db.session.commit()

    #TEAR DOWN - RUNS AFTER TEST
    def tearDown(self):
        db.session.remove()
        db.drop_all()


#testing read functionality

class TestViews(TestBase):
    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

        
class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(
            url_for('signup'),
            data = dict(fname="test", sname="test", kcalaim=8378, date="300518")
        )
        self.assertIn("test", "test", 8378)