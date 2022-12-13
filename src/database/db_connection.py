import sqlite3
from config import DB_FILE_PATH


def get_db_conn(file_path=DB_FILE_PATH):
    connection = sqlite3.connect(file_path)
    return connection
