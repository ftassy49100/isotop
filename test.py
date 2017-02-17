# coding: utf8
from app import db, models
u = models.user.User(firstname=u'François', lastname='Tassy', nickname='ftassy', email='ftassy@matfer.fr')

db.session.add(u)
db.session.commit()

