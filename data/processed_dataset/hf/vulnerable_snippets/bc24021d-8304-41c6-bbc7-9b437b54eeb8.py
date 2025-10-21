from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
    cursor.execute(query)
    
    user = cursor.fetchone()
    if user:
        return 'Logged in successfully', 200
    else:
        return 'Invalid credentials', 401

if __name__ == '__main__':
    app.run(debug=True)
