from ..models.PaymentModel import PaymentModel, db
from flask import request
import json


def add_payment():
    try:
        card_number = request.json['card_number']
        expiry_date = request.json['expiry_date']
        cvv = request.json['cvv']
        user_id = request.json['user_id']
        payment = PaymentModel(
            card_number = card_number,
            expiry_date = expiry_date,
            cvv = cvv,
            user_id = user_id,
        )
        db.session.add(payment)
        db.session.commit()
        return True
    except:
        return False


def view_payments():
    user_id = request.headers.get('user_id')
    payment_data = db.engine.execute(
        "SELECT card_number, expiry_date, cvv FROM payments WHERE user_id=%d;"\
            % (int(user_id))
    )
    return payment_data
