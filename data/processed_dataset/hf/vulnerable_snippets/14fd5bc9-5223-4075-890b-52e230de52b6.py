import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form.get('code')
    eval(code)

if __name__ == "__main__":
    app.run()
