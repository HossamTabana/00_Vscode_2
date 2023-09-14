import sqlite3

conn = sqlite3.connect('file_changes.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM db_track")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()



