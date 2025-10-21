import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    return user

username = input("Enter your username: ")
user_data = get_user_data(username)
print(user_data)
