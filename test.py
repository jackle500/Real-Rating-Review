import nltk
from textblob import TextBlob

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('brown')
nltk.download('wordnet')

def calculate_rating(review):
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity
    rating = (sentiment + 1) * 2.5
    return round(rating, 1)

       