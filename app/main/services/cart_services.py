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
            date = date
        )
        db.session.add(cart)
        db.session.commit()
        return True
    except:
        return False


def view_cart():
    user_id = request.headers.get('user_id')
    cart_data = db.engine.execute(
        "SELECT products.name,products.price,date FROM carts JOIN products \
            ON carts.product_id=products.id WHERE carts.user_id=%d"\
                 % (int(user_id))
    )

    return cart_data
