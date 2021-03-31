from flask import Flask, render_template, redirect, json, jsonify, request

def convertText(text, cipher_type):
    letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_text = ""

    for letter in text:
        current_position = letters.index(letter)
        new_letter = (current_position + int(cipher_type)) % 26
        encrypted_text += letters[new_letter]

    return encrypted_text

###START PAGE ROUTING###
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return_text = "encrypted text shows here"
        return render_template('index.html', return_text=return_text)
    else:
        data = request.form["text"].lower()
        cipher = request.form["cipher_type"]
        return_text = convertText(data, cipher)
        return render_template('index.html', return_text=return_text)

if __name__ == '__main__':
    app.run(port=8000)
###END PAGE ROUTING###