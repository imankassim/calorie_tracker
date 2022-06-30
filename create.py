from application import db
from application.models import UserNew

db.drop_all()
db.create_all()

#test variable
testuser = UserNew(fname="Immy", sname="Kassim", kcalaim=2040, date="300622")
db.session.add(testuser)
db.session.commit()