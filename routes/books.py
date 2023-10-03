# routes/books.py

from flask import Blueprint, render_template, jsonify
from models import Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/allbooks', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])
