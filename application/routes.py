from application import app, db
from application.models import UserNew, Meals
from application.forms import NewUserForm, NewMealForm, Login
from flask import redirect, url_for, render_template, request, Markup
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField


SQLALCHEMY_TRACK_MODIFICATIONS = False

loggedin=False
current_user_id=0
current_user_firstname=""
current_user_surname=""
current_user_kcal=0



@app.route('/', methods=['GET', 'POST'])
@app.route('/login' , methods=['GET', 'POST'])
def login():
    strid=""
    form=Login()
    if request.method == 'POST':
        if form.validate_on_submit():


            current_user = UserNew.query.filter_by(id=(form.chosenid.data), fname=(form.first_name.data) , sname=(form.surname.data)).first()
            if (current_user is not None):
                global loggedin, current_user_firstname, current_user_surname, current_user_kcalaim, current_user_id
                loggedin=True
                current_user_firstname = current_user.fname
                current_user_surname = current_user.sname
                current_user_kcalaim = current_user.kcalaim
                current_user_id = current_user.id
            #test####
                str_all = f'Current user: {current_user}'
                strid = f'id: {current_user_id}'
                strfname = f'fname: {current_user_firstname}'
                strsname = f'name: {current_user_surname}'
                strkcal = f'name: {current_user_kcalaim}'
                return redirect(url_for('home'))
                

                
            else:
                return redirect(url_for('about'))



            # NewUserEntry = UserNew(
            #     fname = form.first_name.data,
            #     sname = form.surname.data,
            #     kcalaim = form.kcalneeded.data
            # )
            
            
    if (strid == ""):
        return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form, strid=strid, strfname=strfname, strsname=strsname, strkcal=strkcal )
    #return render_template('login.html', form=form)



@app.route('/home', methods=['GET', 'POST'])
def home():
    if (current_user_firstname == ""):
        welcomename=""
        userkcal=""
        return redirect(url_for('login'))
    else:
        welcomename = f'Welcome back {current_user_firstname} {current_user_surname}'
        userkcal = f'You need {current_user_kcal} calories today'
    return render_template('home.html', welcomename=welcomename, userkcal=userkcal)


@app.route('/allmeals', methods=['GET', 'POST'])
def allmeals():
    all_meals = Meals.query.all()
    return render_template('UDmealslist.html', meals=all_meals)

@app.route('/allusers', methods=['GET', 'POST'])
def allusers():
    all_users = UserNew.query.all()
    return render_template('UDuserslist.html', users=all_users)




@app.route('/addmeal', methods=['GET', 'POST'])
def addmeal():
    form= NewMealForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            NewMealEntry = Meals(
                mealname = form.mealname.data,
                kcal = form.kcal.data,
                userid = form.userid.data
            )
            db.session.add(NewMealEntry)
            db.session.commit()
            return redirect(url_for('addmeal'))

    return render_template('addmeal.html', form=form)



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
            return redirect(url_for('home'))
    
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
        ##need a new html file for updates only PLEASE... or at least rename this
    return render_template('adduser.html', form=form)


@app.route('/updatemeal/<int:id>', methods=['GET', 'POST'])
def updatemeal(id):
    form=NewMealForm()
    meal_update = Meals.query.get(id)
    if form.validate_on_submit():
        meal_update.mealname = form.mealname.data
        meal_update.kcal = form.kcal.data
        meal_update.userid = form.userid.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method =="GET":
        form.mealname.data = meal_update.mealname
        form.kcal.data = meal_update.kcal
    return render_template('addmeal.html', form=form)

#needs some sort of regulation - password maybe?
@app.route('/delete/<int:id>')
def delete(id):
    user_del = UserNew.query.get(id)
    db.session.delete(user_del)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/deletemeal/<int:id>')
def deletemeal(id):
    meal_del = Meals.query.get(id)
    db.session.delete(meal_del)
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
