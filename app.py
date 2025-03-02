from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

app = Flask(__name__)

# Summarize the text by extracting key sentences based on word frequencies
def summarize_text(text, num_sentences=5):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in word_tokenize(text.lower()) if word.isalnum() and word not in stop_words]
    word_frequencies = Counter(words)
    
    # Score sentences by word frequency
    sentence_scores = {sentence: sum(word_frequencies[word] for word in word_tokenize(sentence.lower()) if word in word_frequencies)
                       for sentence in sentences}
    
    # Get top 'num_sentences' based on score
    return ' '.join(sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    website_url = request.form.get('web_address')
    if not website_url:
        return "No URL provided!"

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(website_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = ' '.join(soup.get_text().split())

        # Summarize the content
        summarized_content = summarize_text(text_content)

    except requests.exceptions.RequestException as e:
        summarized_content = f"<p>Error fetching the website: {e}</p>"

    return render_template('result.html', content=summarized_content)

if __name__ == '__main__':
    app.run(debug=True)
