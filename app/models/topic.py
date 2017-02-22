from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import qualityFolder


class Topic(db.Model):
    __tablename__ = 'it_topic'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('it_topic.id'))
    quality_folders = db.relationship('QualityFolder', backref='topic', lazy="dynamic")

    def __repr__(self):
        return '<Sujet %r>' % (self.name)
