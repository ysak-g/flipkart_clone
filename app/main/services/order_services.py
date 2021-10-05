from ..models.OrderModel import OrderModel, db
from flask import request
import json


def add_order():
    try:
        product_id = request.json['product_id']
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


def view_orders():
    user_id = request.headers.get('user_id')
    order_data = db.engine.execute(
        "SELECT products.name,products.price,date FROM orders JOIN products \
            ON orders.product_id=products.id WHERE orders.user_id=%d" \
                 % (int(user_id))
    )
    return order_data
