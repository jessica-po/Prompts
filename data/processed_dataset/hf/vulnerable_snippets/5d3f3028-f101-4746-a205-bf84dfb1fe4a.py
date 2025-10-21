from flask import Flask, request
app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    result = eval(data['expression'])
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
