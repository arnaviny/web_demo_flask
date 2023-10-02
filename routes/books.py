# routes/books.py

from flask import Blueprint, render_template, jsonify
from models import Book  # אני מניח שיש לך מודל של ספר בפרויקט

books_bp = Blueprint('books', __name__)

@books_bp.route('/allbooks', methods=['GET'])
def get_all_books():
    books = Book.query.all()  # אני מניח שהמודל שלך משתמש ב-SQLAlchemy
    return jsonify([book.to_dict() for book in books])
