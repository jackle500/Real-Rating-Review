from transformers import BartForConditionalGeneration, BartTokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from textblob import TextBlob 

def paraphrase_text(text):
    try:
        # Initialize BART model and tokenizer
        model_name = "facebook/bart-large-cnn"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)
        
        # Tokenize and generate paraphrase
        inputs = tokenizer(text, max_length=1024, truncation=True, return_tensors="pt")
        summary_ids = model.generate(
            inputs["input_ids"],
            num_beams=4,
            length_penalty=2.0,
            max_length=142,
            min_length=56,
            no_repeat_ngram_size=3
        )
        
        paraphrased = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return paraphrased

    except Exception as e:
        print(f"Error in paraphrasing: {e}")
        return text

def summarize_text(review_text, percent=0.3):
    try:
        # Create parser
        parser = PlaintextParser.from_string(review_text, Tokenizer("english"))
        
        # Initialize summarizer
        stemmer = Stemmer("english")
        summarizer = LsaSummarizer(stemmer)
        summarizer.stop_words = get_stop_words("english")
        
        # Calculate number of sentences based on input length
        num_sentences = max(1, len(list(parser.document.sentences)) * percent)
        
        # Generate summary
        summary = summarizer(parser.document, int(num_sentences))
        return " ".join([str(sentence) for sentence in summary])
        
    except Exception as e:
        print(f"Error in summarization: {e}")
        return review_text[:200] + "..."

def summarize_and_paraphrase(review_text, should_paraphrase=True):
    """
    Summarizes and optionally paraphrases the input text
    """
    try:
        # First summarize
        summary = summarize_text(review_text)
        
        # Then paraphrase if requested
        if should_paraphrase:
            return paraphrase_text(summary)
        return summary
        
    except Exception as e:
        print(f"Error in summarize_and_paraphrase: {e}")
        return review_text[:200] + "..."

def analyze_sentiment_points(text):
    try:
        # Initialize sentiment analyzer
        sia = SentimentIntensityAnalyzer()
        
        # Split text into sentences
        sentences = sent_tokenize(text)
        
        positive_points = []
        negative_points = []
        
        for sentence in sentences:
            # Get sentiment scores
            sentiment = sia.polarity_scores(sentence)
            
            # Clean and simplify the sentence using TextBlob
            blob = TextBlob(sentence)
            
            # Categorize based on compound score
            if sentiment['compound'] > 0.2:
                positive_points.append(str(blob))
            elif sentiment['compound'] < -0.2:
                negative_points.append(str(blob))
        
        return {
            'positive': positive_points[:5],  # Limit to top 5 points
            'negative': negative_points[:5]
        }
        
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return {'positive': [], 'negative': []}