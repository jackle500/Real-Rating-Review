from flask import Flask, render_template, request
from test import calculate_rating

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rating = None
    review = None
    if request.method == 'POST':
        review = request.form['review']
        rating = calculate_rating(review)
    return render_template('index.html', rating=rating, review=review)

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=8000, debug=True)