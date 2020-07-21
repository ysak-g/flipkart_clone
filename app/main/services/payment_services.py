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
