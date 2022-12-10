import sqlite3
from config import DB_FILE_PATH


def get_db_conn():
    connection = sqlite3.connect(DB_FILE_PATH)
    return connection
