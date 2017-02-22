from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import attributeType


class Attribute(db.Model):
    __tablename__ = 'it_attribute'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50))
    #attribute_type_id = Column(Integer, ForeignKey('it_attribute_type.id'))
    #attribute_type_owner = relationship("AttributeType", backref="attributes")
    #quality_folder_owner = relationship("QualityFolder", backref="attributes")

    def __repr__(self):
        return '<Type %r>' % (self.value)
