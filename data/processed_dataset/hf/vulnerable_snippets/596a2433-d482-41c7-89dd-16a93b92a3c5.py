from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    os.system(command)
    return 'Command executed'

if __name__ == '__main__':
    app.run(debug=True)
