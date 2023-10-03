import sqlite3

# Connect to the database. This will create a new file named "mydatabase.db"
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a new table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Committing the changes and closing the connection
conn.commit()
conn.close()

import sqlite3

def insert_user(name, age):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    
    conn.commit()
    conn.close()

# Insert a sample user
insert_user("John Doe", 25)
