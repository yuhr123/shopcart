from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='sqlite:///database/shopcart.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
))

db = SQLAlchemy(app)

import shopcart.route
