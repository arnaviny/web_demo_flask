import os


class Config:
    # הגדרות בסיסיות
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'

    # הגדרות התחברות למסד הנתונים
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:your_password@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # הגדרות נוספות יכולות להיכנס כאן
