from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save("/var/www/uploads/" + filename)
    return 'File uploaded successfully!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
