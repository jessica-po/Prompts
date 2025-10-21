from flask import Flask, request
app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def evaluate():
    data = request.get_data()
    result = eval(data)
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
