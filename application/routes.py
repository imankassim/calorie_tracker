from application import app, db
from application.models import UserNew, Meals
from application.forms import NewUserForm
from flask import redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    all_users = UserNew.query.all()
    return render_template('home.html', users = all_users)

# def register():
#     message = ""
#     form = BasicForm()

#     if request.method == 'POST':
#         first_name = form.first_name.data
#         surname = form.surname.data
#         kcalneeded = form.kcalneeded.data

#         if len(first_name) == 0 or len(surname) == 0 or kcalneeded == 0:
#             message = "Please supply all information"
#         else:
#             message = f'Thank you, {first_name} {surname}'

#     return render_template('home.html', form=form, message=message)

#@app.route('/')
# def index():
#     all_users = UserNew.query.all()
#     # userlist = ""
#     # for user in all_users:
#     #     userlist = userlist + (f'Name: {user.fname} {user.sname}, Calories Needed: {user.kcalaim}') 
#     # return userlist
#     return render_template("htmltrial.html", users = all_users)

@app.route('/htmltrial')


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = NewUserForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            NewUserEntry = UserNew(
                fname = form.first_name.data,
                sname = form.surname.data,
                kcalaim = form.kcalneeded.data
            )
            db.session.add(NewUserEntry)
            db.session.commit()
            return redirect(url_for('add'))
    
    return render_template('adduser.html', form=form)

# @app.route('/add/<name>')
# def add(name):
#     new_user = UserNew(fname=name, sname="Kimmy", kcalaim=1987, date="140200")
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect(url_for('home'))


@app.route('/read')
def read():
    all_users = UserNew.query.all()
    user_str = ""
    for user in all_users:
        user_str += "<br>"+user.fname
    return user_str

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form=NewUserForm()
    user_update = UserNew.query.get(id)
    if form.validate_on_submit():
        user_update.fname = form.first_name.data
        user_update.sname = form.surname.data
        user_update.kcalaim = form.kcalneeded.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method =="GET":
        form.first_name.data = user_update.fname
        form.surname.data = user_update.sname
        form.kcalneeded.data = user_update.kcalaim
    return render_template('adduser.html', form=form)

#needs some sort of regulation - password maybe?
@app.route('/delete/<int:id>')
def delete(id):
    user_del = UserNew.query.get(id)
    db.session.delete(user_del)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/count')
def count():
    total = UserNew.query.count()
    return str(total)


















#@app.route('/')

#@app.route('/home/<int:number>')
#def home(number):
#    output = number * number
#    return str(output)

#@app.route('/about')
#def about():
#    return "ABOUT PAGE"


#@app.route('/redirect')
#def redirect1():
#    return "YOU HAVE BEEN REDIRECTED FROM HOME"






#@app.route('/home', methods = ['GET', 'POST'])
#def home():
#    if request.method == 'POST':
#        return "POST method"
#    else:
#        return "GET method"



#@app.route('/home')
#def home():
#    return redirect(url_for('redirect1'))
#
#
#@app.route('/redirect')
#def redirect1():
#    return "YOU HAVE BEEN REDIRECTED FROM HOME"
