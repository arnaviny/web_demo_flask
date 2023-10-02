# routes/categories.py

from flask import Blueprint, render_template, jsonify
from models import Category  # אני מניח שיש לך מודל של קטגוריה בפרויקט

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()  # אני מניח שהמודל שלך משתמש ב-SQLAlchemy
    return jsonify([category.to_dict() for category in categories])