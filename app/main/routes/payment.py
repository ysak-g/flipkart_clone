from flask import Blueprint
from ..services.payment_services import add_payment


payment = Blueprint('payment', __name__)

@payment.route('/')
def home():
    return "Welcome to your payment page"


@payment.route('/add', methods=['POST'])
def new_payment():
    result = add_payment()
    if result:
        return json.dumps({
            "message": "Payment added successfully",
            "status": True
        })
    else:
       return json.dumps({
            "message": "Error while adding payment",
            "status": False
        })
