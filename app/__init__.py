from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)

from controlers import mainController
from controlers import createController
from app import models
from models import qualityFolder
from models import anomalyType
from models import attributeType
from models import user
from models import correctiveAction
from models import curativeAction
from models import preventiveAction
from models import attribute
