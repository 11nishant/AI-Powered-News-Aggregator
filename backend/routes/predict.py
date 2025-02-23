from flask import Blueprint, request, jsonify
from models.text_classifier import predict_conspiracy_score
from models.sentiment_analyzer import analyze_sentiment
from database.db import db
from models.news_model import NewsHeadline


predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    """
    Receives a news headline and returns:
    - Conspiracy Score (0-100%)
    - Sentiment Analysis (Positive/Negative/Neutral)
    """
    try:
        data = request.get_json()
        headline = data.get("headline", "")

        if not headline:
            return jsonify({"error": "No headline provided"}), 400

        # Get Conspiracy Score
        conspiracy_score = int(predict_conspiracy_score(headline))  # 👈 Convert np.int64 to int


        # Get Sentiment
        sentiment, confidence = analyze_sentiment(headline)

        # Save to Database
        new_entry = NewsHeadline(
            headline=headline,
            conspiracy_score=conspiracy_score,
            suspicious_words=[]  # Change if needed
        )
        db.session.add(new_entry)
        db.session.commit()

        # return jsonify({
        #     "headline": headline,
        #     "conspiracy_score": conspiracy_score,
        #     "sentiment": sentiment,
        #     "sentiment_confidence": confidence
        # })


        return jsonify({
            "conspiracy_score": conspiracy_score,
            "headline": headline,
            "sentiment": sentiment,
            "sentiment_confidence": confidence
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
