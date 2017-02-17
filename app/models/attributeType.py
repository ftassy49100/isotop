from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import attribute

class AttributeType(db.Model):
	__tablename__ = 'it_attribute_type'
	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.String(50))
	owned_attributes = relationship("Attribute", backref="attribute_type")


	def __repr__(self):
		return '<Type %r>' % (self.value)

