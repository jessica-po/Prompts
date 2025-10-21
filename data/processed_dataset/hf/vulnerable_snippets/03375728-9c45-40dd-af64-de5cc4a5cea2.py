import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='{}'".format(username)
    result = cursor.execute(query)
    return str(result.fetchone())

if __name__ == '__main__':
    app.run(debug=True)
