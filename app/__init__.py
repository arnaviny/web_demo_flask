from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from .routes import books, reviews, stock, users
    app.register_blueprint(books.bp)
    app.register_blueprint(reviews.bp)
    app.register_blueprint(stock.bp)
    app.register_blueprint(users.bp)

    return app
