from database.db_connection import get_db_conn


def drop_table(conn):
    """Deletes the messgaes table from the database.
    Args:
        conn: Connection object for the database
    """
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS messages;")
    conn.commit()


def create_table(conn):
    """Creates a new table messages.
    Args:
        connection: Connection object for the database
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY,
            recipient TEXT,
            subject TEXT,
            body TEXT
        );
    """)
    conn.commit()


def initialize_database():
    """Initializes a database with a messages table"""

    conn = get_db_conn()
    drop_table(conn)
    create_table(conn)
