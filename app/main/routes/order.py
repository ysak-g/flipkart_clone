from flask import Blueprint
from ..services.order_services import *
import json


order = Blueprint('order', __name__)

@order.route('/')
def home():
    return "Welcome to your orders"


@order.route('/add', methods=['POST'])
def new_order():
    result = add_order()
    if result:
        return json.dumps({
            "message": "Order added successfully",
            "status": True
        })
    else:
       return json.dumps({
            "message": "Error while adding order",
            "status": False
        })


@order.route('/view', methods=['GET'])
def show_order():
    orders = view_orders()
    output = []
    for row in orders:
        item = {}
        item['product_name'] = row['name']
        item['price'] = row['price']
        item['date'] = str(row['date'])
        output.append(item)
    return json.dumps({
        "message": output,
            "status": True
    })
