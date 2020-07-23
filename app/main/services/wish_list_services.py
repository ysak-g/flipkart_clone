from ..models.WishListModel import WishListModel, db
from flask import request
import json


def add_wishlist():
    product_id = request.json['product_id']
    user_id = request.json['user_id']
    wishlist = WishListModel(
        product_id = product_id,
        user_id = user_id
    )
    db.session.add(wishlist)
    db.session.commit()
    return True


def view_wishlist():
    user_id = request.headers.get('user_id')
    wishlist_data = db.engine.execute(
        "SELECT products.name,products.price FROM wish_list JOIN products \
            ON wish_list.product_id=products.id WHERE wish_list.user_id=%d"\
                 % (int(user_id))
    )
    return wishlist_data
