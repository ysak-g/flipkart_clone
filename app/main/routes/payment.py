from flask import Blueprint
from ..services.payment_services import *
import json


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


@payment.route('/view', methods=['GET'])
def show_payment():
    payments = view_payments()
    output = []
    for row in payments:
        item = {}
        item['card_number'] = row['card_number']
        item['expiry_date'] = str(row['expiry_date'])
        item['cvv'] = str(row['cvv'])
        output.append(item)
    return json.dumps({
        "message": output,
            "status": True
    })
