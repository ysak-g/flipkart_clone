from flask import Blueprint
from ..services.cart_services import *
import json


cart = Blueprint('cart', __name__)

@cart.route('/')
def home():
    return "Welcome to your cart"


@cart.route('/add', methods=['POST'])
def new_cart():
    result = add_cart()
    if result:
        return json.dumps({
            "message": "Cart added successfully",
            "status": True
        })
    else:
       return json.dumps({
            "message": "Error while adding cart",
            "status": False
        })


@cart.route('/view', methods=['GET'])
def show_cart():
    carts = view_cart()
    output = []
    for row in carts:
        item = {}
        item['product_name'] = row['name']
        item['price'] = row['price']
        item['date'] = str(row['date'])
        output.append(item)
    return json.dumps({
        "message": output,
            "status": True
    })
