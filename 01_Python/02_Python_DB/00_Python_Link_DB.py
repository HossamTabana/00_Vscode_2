import sqlite3
import pandas as pd

con = sqlite3.connect("Database.db")

cursor = con.cursor()

cursor.execute("Drop table if exists Testing")


cursor.execute("""Create table if not exists Testing(
                Name varchar(255) not null,
                Job varchar(255) not null)""")


cursor.execute ("""Insert into Testing values ('John', 'Programmer'),
                ('Hossam', 'Data Engineer')""")
con.commit()

def fetch_all_users():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Testing")
    users = cursor.fetchall()

    conn.close()

    return users

# Fetch and print all users
users = fetch_all_users()
for user in users:
    print(user)
    
def fetch_all_users_as_dataframe():
    conn = sqlite3.connect('Database.db')
    
    query = "SELECT * FROM Testing"
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    return df

# Fetch and print all users as a DataFrame
df = fetch_all_users_as_dataframe()
print(df)


















