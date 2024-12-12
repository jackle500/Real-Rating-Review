import nltk
from flask import Flask, request, render_template, jsonify
from summarization import summarize_text, analyze_sentiment_points

# Initialize Flask app and set up NLTK
app = Flask(__name__)
nltk.download('punkt')  

def calculate_sentiment_score(positive_count, negative_count):
    """
    Calculate a normalized sentiment score between 0-5 based on positive/negative counts
    A score of 2.5 represents neutral sentiment
    """
    total_count = positive_count + negative_count
    if total_count == 0:
        return 2.5  # Default to neutral if no positive/negative points
    compound_score = (positive_count - negative_count) / total_count
    return (compound_score + 1) * 2.5  

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Main analysis endpoint that processes review text and returns:
    - Summary of the review
    - Overall sentiment (Positive/Neutral/Negative)
    - Numerical score (0-5)
    - Key positive and negative points
    """
    try:
        # Get review text from form data
        review_text = request.form['review']
        if not review_text:
            return jsonify({'error': 'No review text provided'}), 400
            
        # Process the review through ML pipeline
        summarize = summarize_text(review_text)
        key = analyze_sentiment_points(review_text)

        # Calculate overall sentiment score and category
        positive_count = len(key['positive'])
        negative_count = len(key['negative'])
        score = calculate_sentiment_score(positive_count, negative_count)

        # Map numerical score to sentiment category
        sentiment = 'Positive' if score > 3 else 'Negative' if score < 2 else 'Neutral'

        return jsonify({
            'summarize': summarize,
            'sentiment': sentiment,
            'score': score,
            'key': key
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)