import nltk 

# import flask app
from flask import Flask, request, jsonify, render_template
# import sentiment from VADER
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# import text summarizer 
from summarization import summarize_and_paraphrase
# import keypoints extraction
from summarization import analyze_sentiment_points



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
    summarize = summarize_and_paraphrase(review_text)  # Summarize the review
    key = analyze_sentiment_points(review_text)  # Extract key points
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
        'summarize': summarize,
        'key': key   # Return the summary
    })

if __name__ == '__main__':
    app.run(debug=True,port=8080)

    