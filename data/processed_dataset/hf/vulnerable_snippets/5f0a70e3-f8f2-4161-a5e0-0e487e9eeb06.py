import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{query}'")
    results = cursor.fetchall()
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
