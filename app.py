from application import app
import os
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
