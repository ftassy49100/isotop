from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import qualityFolder

class AnomalyType(db.Model):
    __tablename__ = 'it_anomaly_type'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))
    quality_folders = db.relationship('QualityFolder', backref='anomaly_type', lazy='dynamic')

    def __repr__(self):
        return '<%r>' % self.description
