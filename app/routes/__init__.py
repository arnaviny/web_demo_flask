from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# ייבוא המסלולים השונים
from . import books, reviews, stock, users

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


# הרשמה של המסלולים השונים לאפליקציה
app.register_blueprint(books.bp)
app.register_blueprint(reviews.bp)
app.register_blueprint(stock.bp)
app.register_blueprint(users.bp)

# אם יש לך קובץ הגדרות נוסף, כמו config.py, תוכל להוסיף את השורה הבאה:
# app.config.from_object('config')
