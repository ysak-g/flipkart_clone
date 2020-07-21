from ..models.CartModel import CartModel, db
from flask import request
import json


def add_cart():
    try:
        product_id = request.json['product_id']
        date = request.json['date']
        user_id = request.json['user_id']
        cart = CartModel(
            product_id = product_id,
            user_id = user_id,
        )
        db.session.add(cart)
        db.session.commit()
        return True
    except:
        return False
