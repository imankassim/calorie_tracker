from application import db


class UserNew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(10), nullable = False)
    sname = db.Column(db.String(10), nullable = False)
    kcalaim = db.Column(db.Integer, nullable = False)
    #DDMMYY
    date = db.Column(db.String(6), nullable = False)
    meal = db.Column(db.String(50))