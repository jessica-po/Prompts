import sqlite3

def get_user_info(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

# Example usage
print(get_user_info("test' OR '1'='1"))
