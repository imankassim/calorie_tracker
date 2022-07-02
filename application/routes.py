from application import app, db
from application.models import UserNew, Meals
from flask import redirect, url_for, render_template


@app.route('/')
def index():
    all_users = UserNew.query.all()
    userlist = ""
    for user in all_users:
        userlist = userlist + (f'Name: {user.fname} {user.sname}, Calories Needed: {user.kcalaim}') 
    return userlist

@app.route('/htmltrial')
def home():
    userlist = ["immy", "bimmy", "fimmy", "rimbmy", "cimmy", "brimmy"]
    return render_template('htmltrial.html', users=userlist)

@app.route('/add/<name>')
def add(name):
    new_user = UserNew(fname=name, sname="Kimmy", kcalaim=1987, date="140200")
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/read')
def read():
    all_users = UserNew.query.all()
    user_str = ""
    for user in all_users:
        user_str += "<br>"+user.fname
    return user_str

@app.route('/update/<oldname>/<newname>')
def update(oldname, newname):
    first_user = UserNew.query.filter_by(fname=oldname).first()
    first_user.fname = newname
    db.session.commit()
    return first_user.fname


@app.route('/delete/<name>')
def delete(name):
    user_del = UserNew.query.filter_by(fname=name).first()
    db.session.delete(user_del)
    db.session.commit()
    return "First entry deleted"


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
