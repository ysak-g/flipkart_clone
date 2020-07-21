from flask import Blueprint
from ..services.wish_list_services import add_wishlist


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
