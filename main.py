from flask import Flask, render_template, request
from PIL import Image
import os, re, os.path
from predict import predictCaption
from text_speech import textToSpeech

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

            caption = predictCaption()
            f1 = open("static/speech.txt", "w")
            f1.write(caption)
            f1.close()

            output = textToSpeech()

        else:
            return "Select the File"
    return render_template('output.html', path= imagePath, cap=caption)


# mypath = "static/images"
# for root, dirs, files in os.walk(mypath):
#     for file in files:
#         os.remove(os.path.join(root, file))

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(debug=False,host='0.0.0.0', port=port)
    app.run(debug=False)

