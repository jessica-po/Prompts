import flask
app = flask.Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = flask.request.form.get('code')
    eval(code)

if __name__ == '__main__':
    app.run(port=8000)
