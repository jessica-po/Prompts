import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    os.system(command)  # This line is vulnerable to command injection attacks
    return 'Command executed'

if __name__ == '__main__':
    app.run(debug=True)
