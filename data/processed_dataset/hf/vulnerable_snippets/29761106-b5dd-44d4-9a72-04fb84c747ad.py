import flask
app = flask.Flask(__name__)

@app.route('/calc', methods=['GET'])
def calculate():
    equation = flask.request.args.get('equation')
    result = eval(equation)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
