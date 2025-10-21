# Import the necessary module
import flask

# Create a Flask application
app = flask.Flask(__name__)

@app.route('/')
def index():
    # Get the user input from the URL
    user_input = flask.request.args.get('input', '')

    # Evaluate the user input as Python code
    result = eval(user_input)

    # Return the result of the evaluation
    return str(result)

if __name__ == '__main__':
    app.run()
