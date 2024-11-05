# app.py
from flask import Flask, request, jsonify, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Initialize Flask app
app = Flask(__name__)

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review_text = request.form['review']  # Get the review from the form
    score = analyzer.polarity_scores(review_text)  # Analyze sentiment
    sentiment = 'Neutral'  # Default sentiment
    if score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif score['compound'] <= -0.05:
        sentiment = 'Negative'
    
    return jsonify({
        'review': review_text,
        'sentiment': sentiment,
        'score': score
    })

if __name__ == '__main__':
    app.run(debug=True)