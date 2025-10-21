import sqlite3
def fetch_user_data(username):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='{}'".format(username)
    cursor.execute(query)
    row = cursor.fetchone()
    return row

username = input("Enter your username: ")
user_data = fetch_user_data(username)
print(user_data)
