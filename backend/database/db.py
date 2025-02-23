from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """Initialize the database with Flask app."""
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # with app.app_context():
    #     from models.news_model import NewsHeadline  # Import models here
    #     db.create_all()
