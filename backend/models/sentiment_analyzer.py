from transformers import pipeline

# 🟢 Step 1: Load Pre-trained Sentiment Analysis Model
# sentiment_pipeline = pipeline("sentiment-analysis")
# Load model from local directory instead of downloading from Hugging Face


sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="C:/Users/visma/Desktop/news-aggregator/backend/models/distilbert-sentiment"
)

             

# 🟢 Step 2: Define Function for Sentiment Analysis
def analyze_sentiment(text):
    """
    Analyzes sentiment of a given text.
    Returns: (label, confidence_score)
    """
    result = sentiment_pipeline(text)[0]
    return result['label'], round(result['score'], 2)

# 🟢 Step 3: Test the Sentiment Analysis
if __name__ == "__main__":
    test_text = "I love this new scientific discovery!"
    sentiment, score = analyze_sentiment(test_text)
    print(f"Text: {test_text}")
    print(f"Sentiment: {sentiment} (Confidence: {score})")
