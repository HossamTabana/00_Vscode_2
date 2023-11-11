import sqlite3

def fetch_all_users():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return users

# Fetch and print all users
users = fetch_all_users()
for user in users:
    print(user)

