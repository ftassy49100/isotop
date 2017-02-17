from flask import Flask
#from flask_alchemy import SQLAlchemy
from app import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import app