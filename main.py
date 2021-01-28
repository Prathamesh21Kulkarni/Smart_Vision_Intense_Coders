from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import io
import base64
from PIL import Image


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.files['my_image']
        if img:
            image = Image.open(img.stream)

            imagePath = "static/images/" + img.filename
            f = open("static/imageExt.txt", "w")
            f.write(imagePath)
            f.close()
            image.save(imagePath)
           
        else:
            return "Select the File"
    return render_template('output.html', path= imagePath)


app.run(debug=True)
