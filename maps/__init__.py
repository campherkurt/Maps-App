from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from settings import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from maps import views, models


