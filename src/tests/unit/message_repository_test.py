
import os
import unittest
from database.db_connection import get_db_conn
from database.init_db import initialize_db

from repositories.message_repository import MessageRepository


class TestMessageRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        test_db_path = os.path.join(
            dirname, '..', '..', '..', 'data', 'test.sqlite')
        self.connection = get_db_conn(test_db_path)
        initialize_db(self.connection)
        self.msg_repo = MessageRepository(self.connection)

    def test_create(self):
        self.msg_repo.create("test@test.com", "test", "test message")
        messages = self.msg_repo.get_all_subjects()

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["subject"], "test")

    def test_edit(self):
        self.msg_repo.create("test@test.com", "test1", "test message")
        messages = self.msg_repo.get_all_subjects()
        self.assertEqual(len(messages), 1)

        self.msg_repo.edit(
            messages[0]["id"], "edited_to", "edited_subject", "edited_body")
        message = self.msg_repo.get_by_id(messages[0]["id"])

        self.assertEqual(message["to"], "edited_to")
        self.assertEqual(message["subject"], "edited_subject")
        self.assertEqual(message["body"], "edited_body")

    def test_get_all_subjects(self):
        self.msg_repo.create("test@test.com", "test1", "test message")
        self.msg_repo.create("test@test.com", "test2", "test message")
        messages = self.msg_repo.get_all_subjects()

        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]["subject"], "test1")
        self.assertEqual(messages[1]["subject"], "test2")

    def test_get_by_id(self):
        self.msg_repo.create("test@test.com", "test1", "test message")
        messages = self.msg_repo.get_all_subjects()
        self.assertEqual(len(messages), 1)
        message = self.msg_repo.get_by_id(messages[0]["id"])

        self.assertEqual(message["to"], "test@test.com")
        self.assertEqual(message["subject"], "test1")
        self.assertEqual(message["body"], "test message")

    def test_delete(self):
        self.msg_repo.create("test@test.com", "test1", "test message")
        messages = self.msg_repo.get_all_subjects()
        self.assertEqual(len(messages), 1)

        self.msg_repo.delete(messages[0]["id"])
        messages = self.msg_repo.get_all_subjects()
        self.assertEqual(len(messages), 0)
