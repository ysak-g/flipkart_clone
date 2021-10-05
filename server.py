from app.main import create_app, db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.main.models import *
from flask import render_template

config_name = "development"

app = create_app(config_name)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html")

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
