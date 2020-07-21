from flask import Blueprint
from ..services.cart_services import add_cart


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
