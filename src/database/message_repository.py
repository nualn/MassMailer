from database.db_connection import get_db_conn


class MessageRepository:
    def __init__(self, conn):
        self._conn = conn

    def get_all_subjects(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT id, subject FROM messages;")
        messages = cursor.fetchall()
        return list(map(lambda x: {"id": x[0], "subject": x[1]}, messages))

    def get_by_msg_id(self, msg_id):
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT recipient, subject, body FROM messages WHERE id = ?;",
            (msg_id,)
        )
        message = cursor.fetchone()
        return {"to": message[0], "subject": message[1], "body": message[2]}

    def create(self, recipient, subject, body):
        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO messages (recipient, subject, body) values (?,?,?);",
            (recipient, subject, body)
        )
        self._conn.commit()

    def edit(self, msg_id, recipient, subject, body):
        cursor = self._conn.cursor()
        cursor.execute("""UPDATE messages SET
            recipient = ?, 
            subject = ?,
            body = ?
            WHERE id = ?;""",
                       (recipient, subject, body, msg_id)
                       )
        self._conn.commit()

    def delete(self, msg_id):
        cursor = self._conn.cursor()
        cursor.execute(
            "DELETE FROM messages WHERE id = ?;",
            (msg_id,)
        )
        self._conn.commit()


message_repository = MessageRepository(get_db_conn())
