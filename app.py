# import flask app
from flask import Flask, request, jsonify, render_template
# import sentiment from VADER
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
# import text summarizer 
from summarization import summarize_text

# Initialize Flask app
app = Flask(__name__)

# Download VADER lexicon d
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review_text = request.form['review']  # Get the review from the form
    summarize = summarize_text(review_text)
    score = analyzer.polarity_scores(review_text)  # Analyze sentiment
    sentiment = 'Neutral'  # Default sentiment
   
    if score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif score['compound'] <= -0.05:
        sentiment = 'Negative'
    
    return jsonify({
        'review': review_text,
        'sentiment': sentiment,
        'score': score,
        'summarize':summarize
    })

if __name__ == '__main__':
    app.run(debug=True,port=8080)

