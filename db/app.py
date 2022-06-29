import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##change for RISK!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")


db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=true)