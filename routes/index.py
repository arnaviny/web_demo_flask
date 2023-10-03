from flask import Blueprint, render_template, jsonify
from models import Book  # אני מניח שיש לך מודל של ספר בפרויקט

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def home():
    return "Hello, World!"

@index_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()  # אני מניח שהמודל שלך משתמש ב-SQLAlchemy
    return jsonify([book.to_dict() for book in books])

@index_bp.route('/bestbook', methods=['GET'])
def get_best_rated_book():
    best_book = Book.query.order_by(Book.rating.desc()).first()
    return jsonify(best_book.to_dict() if best_book else {})
