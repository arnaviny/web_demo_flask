# routes/search.py

from flask import Blueprint, render_template, jsonify, request
from models import Book  # אני מניח שיש לך מודל של ספר בפרויקט

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    books = Book.query.filter(Book.title.contains(query)).all()  # אני מניח שהמודל שלך משתמש ב-SQLAlchemy
    return jsonify([book.to_dict() for book in books])
