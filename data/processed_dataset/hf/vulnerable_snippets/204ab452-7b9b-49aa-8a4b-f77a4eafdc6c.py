import sqlite3

def get_user_info(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='%s'" % username
    cursor.execute(query)
    return cursor.fetchone()

# Example usage
print(get_user_info("john"))
