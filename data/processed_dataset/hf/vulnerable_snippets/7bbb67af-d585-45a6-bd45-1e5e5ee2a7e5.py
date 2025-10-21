import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template_string('Hello, {{ user }}', user=flask.request.args.get('user', 'guest'))

@app.route('/unsafe')
def unsafe():
    user_input = flask.request.args.get('user')
    return eval(user_input)

if __name__ == '__main__':
    app.run()
