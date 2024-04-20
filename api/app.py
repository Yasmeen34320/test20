import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# # Set the path to Tesseract executable (update this with your actual Tesseract path)
#pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


@app.route('/')
def hello():
    return "<h1>Hello, World!! </h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

