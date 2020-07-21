from .. import db
from sqlalchemy import Table, Column, Integer, ForeignKey
import datetime


class PaymentModel(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(50))
    expiry_date = db.Column(db.DateTime)
    cvv = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
