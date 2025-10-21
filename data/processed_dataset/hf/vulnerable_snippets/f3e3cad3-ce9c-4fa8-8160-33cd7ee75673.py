import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user/<username>')
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    result = cursor.execute(query)
    return result.fetchone()

if __name__ == '__main__':
    app.run(debug=True)
