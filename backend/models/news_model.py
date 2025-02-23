from database.db import db

class NewsHeadline(db.Model):
    __tablename__ = "news_headlines"

    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.Text, nullable=False)
    conspiracy_score = db.Column(db.Float, nullable=False)
    suspicious_words = db.Column(db.JSON, default=[])

    def __repr__(self):
        return f"<NewsHeadline {self.headline}>"
