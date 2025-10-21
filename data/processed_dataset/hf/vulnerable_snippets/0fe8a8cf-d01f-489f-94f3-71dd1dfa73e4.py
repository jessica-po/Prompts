import sqlite3
def fetch_user_data(username):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='{}'".format(username)
    cursor.execute(query)
    user_data = cursor.fetchone()
    return user_data
