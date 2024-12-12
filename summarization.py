from transformers import BartForConditionalGeneration, BartTokenizer, pipeline
from nltk.tokenize import sent_tokenize

# Load BART model for text summarization
# We use facebook/bart-large-cnn as it's optimized for summarization tasks
summarization_model_name = "facebook/bart-large-cnn"
summarization_tokenizer = BartTokenizer.from_pretrained(summarization_model_name)
summarization_model = BartForConditionalGeneration.from_pretrained(summarization_model_name)

def summarize_text(text):
    """
    Generate a concise summary of the input text using BART.
    """
    if not text or not text.strip():
        return "No text provided for summarization."
    
    try:
        # Tokenize and encode the input text
        inputs = summarization_tokenizer.batch_encode_plus(
            [text],
            return_tensors='pt',
            max_length=1024,  # BART's max input length
            truncation=True
        )
        
        if not inputs or 'input_ids' not in inputs:
            raise ValueError("Failed to encode input text")
            
        # Generate summary with beam search for better quality
        summary_ids = summarization_model.generate(
            inputs['input_ids'],
            num_beams=4,  # Use beam search with 4 beams
            max_length=400,  # Keep summary reasonably sized
            early_stopping=True
        )
        
        summary = summarization_tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )
        
        if not summary:
            raise ValueError("Generated summary is empty")
            
        return summary
        
    except ValueError as ve:
        print(f"ValueError in summarization: {ve}")
        return "Error: Unable to generate summary."
    except Exception as e:
        print(f"Unexpected error in summarization: {e}")
        return text[:200] + "..."  # Fallback to text truncation

# Initialize BERT model for sentiment analysis
sentiment_pipeline = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

def analyze_sentiment_points(text):
    """
    Break down text into sentences and analyze sentiment of each one.
    Returns top 5 positive and negative points based on sentiment scores.
    """
    try:
        # Split text into individual sentences for analysis
        sentences = sent_tokenize(text)
        positive_points = []
        negative_points = []
        
        # Analyze each sentence and categorize based on rating
        for sentence in sentences:
            result = sentiment_pipeline(sentence)[0]
            label = result['label']
            rating = int(label.split()[0])  # Extract numerical rating (1-5)
            
            # Categorize as positive (4-5) or negative (1-2)
            if rating >= 4:
                positive_points.append(sentence)
            elif rating <= 2:
                negative_points.append(sentence)
                
        return {
            'positive': positive_points[:5],  # Return top 5 points
            'negative': negative_points[:5]
        }
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return {'positive': [], 'negative': []}