from flask import Flask
from config import app_config
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.main.routes.order import order
from app.main.routes.cart import cart
from app.main.routes.payment import payment
from app.main.routes.comment import comment
from app.main.routes.wishlist import wishlist
from app.main.routes.user import user
from app.main.routes.about import about

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(about, url_prefix='/about')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(order, url_prefix='/order')
    app.register_blueprint(cart, url_prefix='/cart')
    app.register_blueprint(payment, url_prefix='/payment')
    app.register_blueprint(comment, url_prefix='/comment')
    app.register_blueprint(wishlist, url_prefix='/wishlist')
    return app
