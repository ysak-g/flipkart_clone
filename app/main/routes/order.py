from flask import Blueprint
from ..services.order_services import add_order


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
