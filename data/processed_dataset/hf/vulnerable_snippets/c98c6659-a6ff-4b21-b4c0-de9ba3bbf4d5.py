import os
import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form.get('code')
    sanitized_code = re.sub(r'\b(os|sys|eval)\b', '', code)
    exec(sanitized_code)
    return 'Code executed successfully!'

if __name__ == '__main__':
    app.run(debug=True)
