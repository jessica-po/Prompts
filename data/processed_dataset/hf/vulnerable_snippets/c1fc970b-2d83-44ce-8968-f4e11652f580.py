import sqlite3

def fetch_user_data(username):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # User input is directly used to construct SQL queries
    query = "SELECT * FROM users WHERE username='{}'".format(username)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# Vulnerable call
fetch_user_data("admin' OR '1'='1")
