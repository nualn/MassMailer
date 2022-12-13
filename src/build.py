from database.db_connection import get_db_conn
from database.init_db import initialize_db


def build():
    conn = get_db_conn()
    initialize_db(conn)


if __name__ == "__main__":
    build()
