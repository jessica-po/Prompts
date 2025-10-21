from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    command = request.args.get('command', '')
    eval(command)

if __name__ == '__main__':
    app.run(debug=True)
