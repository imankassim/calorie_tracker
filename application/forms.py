from application import app, db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired


class UserCheck:
    def __init__(self, banned, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.        
        self.banned = banned        
        if not message:
            message = 'Please choose another name' # If no message chosen, then this default message is returned.        
        self.message = message    
    
    def __call__(self, form, field):
        # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.        
            if field.data.lower() in (word.lower() for word in self.banned):
                raise ValidationError(self.message)

class NumCheck:
    def __init__(self, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.              
        if not message:
            message = 'Enter correct calorie amount' # If no message chosen, then this default message is returned.        
        self.message = message    
    
    def __call__(self, form, field):
        # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.        
            if (field.data > 50000):
                    raise ValidationError(self.message)




class NewUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), UserCheck(message="meal is banned, try another", banned = ['root', 'admin', 'sys'])])
    surname = StringField("Surname", validators=[DataRequired(), UserCheck(message="meal is banned, try another", banned = ['root', 'admin', 'sys'])])
    kcalneeded = IntegerField("Calories Needed", validators=[DataRequired(message="You must enter a valid calorie number that is more than 0"), NumCheck(message="Enter correct calories")])
    submit = SubmitField("Submit Details")


class NewMealForm(FlaskForm):
    mealname = StringField("Enter the name of your meal", validators=[DataRequired(), UserCheck(message="meal is banned, try another", banned = ['root', 'admin', 'sys'])])
    kcal = IntegerField("Calories in the meal", validators=[DataRequired(message="You must enter a valid calorie number that is more than 0"), NumCheck(message="Enter correct calories")])
    userid = IntegerField("What is your User ID?")
    submit = SubmitField("Submit Details")

class Login(FlaskForm):
    chosenid = IntegerField("Enter your ID", validators=[DataRequired(message="You must enter a valid ID number"), NumCheck(message="You must enter a valid ID number")])
    first_name = StringField("First Name", validators=[DataRequired(), UserCheck(message="meal is banned, try another", banned = ['root', 'admin', 'sys'])])
    surname = StringField("Surname", validators=[DataRequired(), UserCheck(message="meal is banned, try another", banned = ['root', 'admin', 'sys'])])
    submit = SubmitField("Submit Details")

