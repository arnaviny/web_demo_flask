from flask import Blueprint, render_template, jsonify
from models import Book

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def home():
    return render_template('index.html')

@index_bp.route('/bestbook', methods=['GET'])
def get_best_rated_book():
    best_book = Book.query.order_by(Book.rating.desc()).first()
    return jsonify(best_book.to_dict() if best_book else {})
