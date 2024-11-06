from textblob import TextBlob

def summarize_review(review_text):
    # Use TextBlob to analyze the text and split it into sentences
    blob = TextBlob(review_text)
    sentences = blob.sentences

    # Get the main points by selecting key sentences (in this case, the first and last sentence for simplicity)
    if len(sentences) > 2:
        summary = sentences[0] + " ... " + sentences[-1]
    else:
        summary = review_text  # For shorter texts, just return the original

    return str(summary)

def summarize_text(text):
    return summarize_review(text)  # Call the existing summarize_review function


text = "Well built and sturdy. Theres a bit of noise from the hard drives, but the enclosure is quiet. Super easy to use and looks great."
print(summarize_text(text))

