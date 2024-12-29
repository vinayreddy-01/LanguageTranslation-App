from flask import Flask, render_template, request, flash
from langdetect import detect
from googletrans import LANGUAGES
from googletrans import Translator

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Helper function for detecting and translating
def detect_and_translate(text, target_lang):
    result_lang = detect(text)
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang).text
    return result_lang, translate_text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""
    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']

        if not text or not target_lang:
            flash("Please fill out all fields!", 'error')
        else:
            detected_lang, translation = detect_and_translate(text, target_lang)
            flash("Translation successful!", 'success')

    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
