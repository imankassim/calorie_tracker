from application import db
from application.models import UserNew, Meals

db.drop_all()
db.create_all()

#test variable
testuser = UserNew(fname="Immy", sname="Kassim", kcalaim=2040, date="300622")
testuser2 = UserNew(fname="Iefdsmmy", sname="Ksfassim", kcalaim=2020, date="300622")

meal1 = Meals(mealname = "Chicken Pot Pie", kcal = 340)
#userid=testuser.id
db.session.add(testuser)
db.session.add(testuser2)
db.session.add(meal1)
db.session.commit()

# print(testuser.id, testuser.fname, testuser.kcalaim)
# print(meal1.mealname, meal1.kcal)