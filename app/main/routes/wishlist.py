from flask import Blueprint
from ..services.wish_list_services import *
import json


wishlist = Blueprint('wishlist', __name__)

@wishlist.route('/')
def home():
    return "Welcome to your wishlist"


@wishlist.route('/add', methods=['POST'])
def new_wishlist():
    result = add_wishlist()
    if result:
        return json.dumps({
            "message": "Wishlist added successfully",
            "status": True
        })
    else:
       return json.dumps({
            "message": "Error while adding wishlist",
            "status": False
        })


@wishlist.route('/view', methods=['GET'])
def show_wishlist():
    wishlist = view_wishlist()
    output = []
    for row in wishlist:
        item = {}
        item['product_name'] = row['name']
        item['price'] = row['price']
        output.append(item)
    return json.dumps({
        "message": output,
            "status": True
    })
