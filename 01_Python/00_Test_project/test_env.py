import os
from dotenv import load_dotenv

load_dotenv()  # This will load environment variables from .env file

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Now you can use DB_USER and DB_PASS in your SQL connection code
print(DB_USER)
print(DB_PASS)
