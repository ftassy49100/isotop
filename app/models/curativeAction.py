from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import qualityFolder


class CurativeAction(db.Model):
    __tablename__ = 'it_curative_action'
    id = db.Column(db.Integer, primary_key=True)
    quality_folder_id = db.Column(db.Integer, db.ForeignKey('it_quality_folder.id'))
    accountant_id = db.Column(db.Integer, db.ForeignKey('it_user.id'))
    analysis = db.Column(db.String(800))
    immediate = db.Column(db.Boolean, default=False)
    consequences = db.Column(db.String(800))
    notes = db.Column(db.String(800))
    predicted_date = db.Column(db.DateTime)
    ending_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<curative %r>' % (self.id)
