import sqlite3
import pandas as pd

# Create the connection
conn = sqlite3.connect('file_changes.db')

# Use pandas to run SQL query and put the results into a DataFrame
df = pd.read_sql_query("SELECT * FROM db_track", conn)

print(df)

# Always remember to close the connection
conn.close()
