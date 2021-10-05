from .. import db


class AddressModel(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200))
    locality = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(50))
    landmark = db.Column(db.String(200))
