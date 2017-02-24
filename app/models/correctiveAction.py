from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import qualityFolder
import user


class CorrectiveAction(db.Model):
    __tablename__ = 'it_corrective_action'
    id = db.Column(db.Integer, primary_key=True)
    # QualityFolder relationship #
    quality_folder_id = db.Column(db.Integer, db.ForeignKey('it_quality_folder.id'))
    ##############################
    #### Users relationships #####
    pilot_id = db.Column(db.Integer, db.ForeignKey('it_user.id'))
    pilot_by = relationship('User', foreign_keys=[pilot_id])
    defined_by_id = db.Column(db.Integer, db.ForeignKey('it_user.id'))
    defined_by_user = relationship('User', foreign_keys=[defined_by_id])
    led_by_id = db.Column(db.Integer, db.ForeignKey('it_user.id'))
    led_by_user = relationship('User', foreign_keys=[led_by_id])
    set_up_by_id = db.Column(db.Integer, db.ForeignKey('it_user.id'))
    set_up_by_user = relationship('User', foreign_keys=[set_up_by_id])
    ##############################
    cause = db.Column(db.String(800))
    to_do = db.Column(db.String(800))

    predicted_date = db.Column(db.DateTime)
    ending_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Corrective %r>' % (self.id)
