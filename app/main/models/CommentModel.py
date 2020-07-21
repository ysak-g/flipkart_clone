from .. import db
from sqlalchemy import Table, Column, Integer, ForeignKey


class CommentModel(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200))
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
