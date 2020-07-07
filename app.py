# Importing essential libraries
from flask import Flask, render_template, request
from googletrans import Translator

translator=Translator()

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    lang=request.form['languages']
    lang=lang.lower()
    if(lang=="kannada"):
        dest_code='kn'
    if(lang=="japanese"):
        dest_code='ja'
    if(lang=="hindi"):
        dest_code='hi'
    if(lang=="telugu"):
        dest_code='te'   
    if(lang=="tamil"):
        dest_code='ta'        
    text_to_translate = translator.translate(message, src= 'en', dest= dest_code)
    text = text_to_translate.text  
    return render_template('index.html', prediction=text)    



if __name__ == '__main__':
	app.run(debug=True)