import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
    cursor.execute(query)
    
    if cursor.fetchone() is not None:
        return "Login successful!"
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
    app.run(debug=True)
