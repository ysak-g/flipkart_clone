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
