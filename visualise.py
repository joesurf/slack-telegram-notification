# Run slack and telegram bots
import os
import logging
import requests
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
import emoji

from database import create_db_connection


# Initialising credentials 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

host = os.environ.get("DB_HOST")
user = "admin"
password = os.environ.get("DB_PASS") 
database = "teleslack"


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name, user=user_name, password=user_password, database=db_name) 
        print("MySQL Database connection successful")
    except pymysql.Error as e:
        print(f"Error: '{e}'")
    return connection


connection = create_db_connection(host, user, password, database)
cursor = connection.cursor()
cursor.execute(f'SELECT COUNT(chat_id) FROM Profile WHERE chat_id IS NOT NULL')

