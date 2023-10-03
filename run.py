from flask import Flask
from routes import books, categories, index, search
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_password@localhost:5432/your_database_name'
db = SQLAlchemy(app)

app.register_blueprint(books.books_bp)
app.register_blueprint(categories.categories_bp)
app.register_blueprint(index.index_bp)
app.register_blueprint(search.search_bp)

if __name__ == "__main__":
    app.run(debug=True)
