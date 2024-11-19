# Real-Rating-Review

## Setup Instructions

   1. Clone the repository:
      
      git clone https://github.com/jackle500/Real-Rating-Review.git

   2. Create a virtual environment:

      python -m venv env
      source env/bin/activate  # On Windows use `env\Scripts\activate`


   3. Install the dependencies:
  
      pip install -r requirements.txt

   4. Download necessary NLTK data:

      python -m nltk.downloader vader_lexicon

   5. Run the Flask app:

      python3 app.py
