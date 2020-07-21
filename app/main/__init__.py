from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.main.routes.order import order
from app.main.routes.cart import cart
from app.main.routes.payment import payment
from app.main.routes.comment import comment
from app.main.routes.wishlist import wishlist


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        "mysql://root:ysak123@localhost/flipkart"
    db.init_app(app)
    app.register_blueprint(order, url_prefix='/order')
    app.register_blueprint(cart, url_prefix='/cart')
    app.register_blueprint(payment, url_prefix='/payment')
    app.register_blueprint(comment, url_prefix='/comment')
    app.register_blueprint(wishlist, url_prefix='/wishlist')
    return app
