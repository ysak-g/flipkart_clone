from ..models.OrderModel import OrderModel, db
from flask import request
import json


def add_order():
    try:
        product_id = request.json['name']
        date = request.json['date']
        user_id = request.json['user_id']
        order = OrderModel(
            product_id = product_id,
            date = date,
            user_id = user_id,
        )
        db.session.add(order)
        db.session.commit()
        return True
    except:
        return False
