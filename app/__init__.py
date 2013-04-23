from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Import settings from config.py
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views,models