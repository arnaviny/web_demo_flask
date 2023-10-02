from flask import Blueprint, jsonify, request
from app.models.book import Book
from app import db

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books])

@bp.route('/add', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!"}), 201
