from flask import Blueprint, request, jsonify
from database.db import db
from models.news_model import NewsHeadline

news_bp = Blueprint('news', __name__)

@news_bp.route('/news', methods=['GET'])
def get_news():
    """Retrieve all news headlines."""
    try:
        news = NewsHeadline.query.all()
        return jsonify([{
            "id": n.id,
            "headline": n.headline,
            "score": n.conspiracy_score
        } for n in news])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@news_bp.route('/news', methods=['POST'])
def add_news():
    """Add a new news headline."""
    try:
        data = request.get_json()

        if not data or "headline" not in data or "conspiracy_score" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        new_headline = NewsHeadline(
            headline=data["headline"],
            conspiracy_score=data["conspiracy_score"]
        )
        db.session.add(new_headline)
        db.session.commit()

        return jsonify({"message": "News added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@news_bp.route('/news/<int:id>', methods=['PUT'])
def update_news(id):
    """Update a news headline."""
    try:
        data = request.get_json()
        news = NewsHeadline.query.get_or_404(id)

        if "conspiracy_score" in data:
            news.conspiracy_score = data["conspiracy_score"]

        db.session.commit()
        return jsonify({"message": "News updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@news_bp.route('/news/<int:id>', methods=['DELETE'])
def delete_news(id):
    """Delete a news headline."""
    try:
        news = NewsHeadline.query.get_or_404(id)
        db.session.delete(news)
        db.session.commit()
        return jsonify({"message": "News deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
