from .. import db
from sqlalchemy import Table, Column, Integer, ForeignKey


class CartModel(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
