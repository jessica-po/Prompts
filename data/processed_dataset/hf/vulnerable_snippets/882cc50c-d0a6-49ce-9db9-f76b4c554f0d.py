import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def my_form():
    return '''
        <form method="POST">
            <input name="text">
            <input type="submit">
        </form>'''

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    eval(text)
    return ''

if __name__ == "__main__":
    app.run()
