import sqlite3

def get_user_info(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username='{}'".format(username)
    cursor.execute(query)
    
    result = cursor.fetchone()
    return result

# Test
print(get_user_info("admin"))
