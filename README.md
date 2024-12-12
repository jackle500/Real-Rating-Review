# Real-Rating-Review

## Overview
Real-Rating-Review is an AI-powered web application that analyzes product reviews using advanced natural language processing. It provides users with intelligent insights through summarization and sentiment analysis.

## Key Features

### 1. Review Summarization
- Condenses long reviews into concise, meaningful summaries
- Maintains key information while reducing length
- Uses BART (facebook/bart-large-cnn) model for accurate summarization

### 2. Sentiment Analysis
- Analyzes the emotional tone of reviews
- Provides a sentiment score (0-5 scale)
- Categorizes sentiment as Positive, Neutral, or Negative
- Visual representation through star ratings

### 3. Key Points Extraction
- Automatically identifies positive and negative aspects
- Extracts up to 5 positive points from the review
- Extracts up to 5 negative points from the review
- Displays points with intuitive icons (✓ for positive, ✗ for negative)

### 4. User Interface
- Clean, modern design with responsive layout
- Real-time analysis and results display
- Interactive cards with hover effects
- Mobile-friendly interface

## Technical Stack
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **ML Models**: 
  - BART for summarization
  - BERT for sentiment analysis
- **Libraries**: 
  - transformers
  - nltk
  - Flask

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation Steps

1. Clone the repository:

2. Create an environemnt

# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate

3. Install requirement packages:

pip install -r requirements.txt

4. Run the app.py

python app.py

   
### Access the application:

Open your web browser and go to http://localhost:8080.

# Paste any review into the input field and click analyze

# The front-end will give you: 

   # A Summarize of the review, generates a coherent summary that captures the main points

   # A sentiment score from 0 to 5, and stars that reflect the score
      Score range is indeed 0-5 where:
      0-1: Very negative
      1-2: Negative
      2-3: Neutral
      3-4: Positive
      4-5: Very positive

      Stars visualization:
      ★★★★★ (5 full stars) = score 4.5-5.0
      ★★★★☆ (4 stars) = score 3.5-4.4
      ★★★☆☆ (3 stars) = score 2.5-3.4
      etc.

   # Key Points Extraction:
      Each sentence gets its own sentiment score (1-5)
      Positive points: Sentences with scores ≥ 4
      Negative points: Sentences with scores ≤ 2
      Maximum 5 points each category
      Displayed with icons:
      ✓ (green check) for positive points
      ✗ (red x) for negative points

# Project Structure
app.py: Main Flask application file.
summarization.py: Contains functions for summarization, paraphrasing, and sentiment analysis.
templates/: Directory containing HTML templates.
static/: Directory containing CSS and JavaScript files.
test_summarization.py: Test cases for the summarization module.
requirements.txt: Python dependencies.