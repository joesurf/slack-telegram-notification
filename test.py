from database import create_db_connection


# Run slack and telegram bots
import os
from pathlib import Path

from dotenv import load_dotenv




# Initialising credentials 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

host = os.environ.get("DB_HOST")
user = "admin"
password = os.environ.get("DB_PASS") 
database = "teleslack"


connection = create_db_connection(host, user, password, database)
cursor = connection.cursor()


connection.commit()
connection.close()