import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
        results = cursor.execute(query).fetchall()

        if len(results) > 0:
            return "Login Successful!"
        else:
            return "Invalid credentials!"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
