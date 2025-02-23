from flask import Flask
from flask_cors import CORS
from database.db import db, init_db
from config import Config
from routes.predict import predict_bp
from routes.news_crud import news_bp

app = Flask(__name__)
CORS(app) # Enable CORS for frontend integration
app.config.from_object(Config)

# Initialize database
init_db(app)

# Register Blueprints (Routes)
# app.register_blueprint(predict_bp)
# app.register_blueprint(news_bp)

app.register_blueprint(predict_bp, url_prefix='/api')
app.register_blueprint(news_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the News Aggregator API!"


if __name__ == "__main__":
    app.run(debug=True)
