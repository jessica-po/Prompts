import flask

app = flask.Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = flask.request.get_json()
    result = eval(data['expression'])
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
