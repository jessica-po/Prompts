import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_data()
    deserialized_data = pickle.loads(data)
    print(deserialized_data)
    return 'OK'

if __name__ == "__main__":
    app.run(debug=True)
