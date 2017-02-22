from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import qualityFolder


class Topic(db.Model):
    """" Topic concerned by the Quality Folder. 1 topic to N folders """
    __tablename__ = 'it_topic'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('it_topic.id'))
    quality_folders = db.relationship('QualityFolder', backref='topic', lazy="dynamic")

    @staticmethod  # return a list usable for forms
    def form_list():
        topics = Topic.query.all()
        topics_list = []
        for topic in topics:
            topics_list.append((unicode(topic.id), unicode(topic.name)))
        return topics_list

    def __repr__(self):
        return '<Sujet %r>' % (self.name)
