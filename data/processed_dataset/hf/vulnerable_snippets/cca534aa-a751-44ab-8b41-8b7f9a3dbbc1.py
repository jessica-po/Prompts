from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to my website!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form.get('data')
    result = eval(data)
    return "Result: {}".format(result)

if __name__ == '__main__':
    app.run()
