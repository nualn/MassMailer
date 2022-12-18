
import os
import unittest
from unittest.mock import Mock
from app.app import App
from database.db_connection import get_db_conn
from database.init_db import initialize_db
from google_api.gmail_service import GmailService
from repositories.message_repository import MessageRepository
from utils.text_parser import parser


class TestSendAll(unittest.TestCase):
    def setUp(self):
        self.auth = Mock()

        self.build_function = Mock()
        self.build_function().users().getProfile(userId='me').execute.return_value = {
            'emailAddress': 'test@gmail.com'
        }
        self.mail_service = GmailService(self.build_function)
        creds = {'some': 'credentials'}
        self.mail_service.build(creds)

        self.parser = parser

        dirname = os.path.dirname(__file__)
        test_db_path = os.path.join(
            dirname, '..', '..', '..', 'data', 'test.sqlite')
        self.connection = get_db_conn(test_db_path)
        initialize_db(self.connection)
        self.message_repository = MessageRepository(self.connection)

        self.app = App(self.auth, self.mail_service,
                       self.parser, self.message_repository)

    def test_mass_send(self):
        message = {
            'to': 'to [1]',
            'subject': 'subject [2]',
            'body': 'body [1] [2] [3]'
        }
        message_encoded = 'Q29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1dGYtOCIKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdApNSU1FLVZlcnNpb246IDEuMApGcm9tOiB0ZXN0QGdtYWlsLmNvbQpUbzogdG8gZGF0YTEKU3ViamVjdDogc3ViamVjdCBkYXRhMgoKYm9keSBkYXRhMSBkYXRhMiBkYXRhMwo='

        rows = [{'1': 'data1', '2': 'data2', '3': 'data3'}]
        self.app.mass_send(message, rows)

        self.mail_service.get_service().users().messages().send.assert_called_once_with(
            userId='me',
            body={'raw': message_encoded}
        )

    def test_save_and_load_message(self):
        message = {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        }
        self.app.save_message(message)

        subjects = self.app.list_messages()
        self.assertEqual(len(subjects), 1)

        saved_message = self.app.load_message(subjects[0]['id'])

        self.assertEqual(saved_message, message)

    def test_edit_message(self):
        original_message = {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        }
        self.app.save_message(original_message)

        edited_message = {
            'to': 'edited to',
            'subject': 'edited subject',
            'body': 'edited body'
        }

        subjects = self.app.list_messages()
        self.assertEqual(len(subjects), 1)

        self.app.edit_message(subjects[0]['id'], edited_message)

        subjects = self.app.list_messages()
        self.assertEqual(len(subjects), 1)

        saved_message = self.app.load_message(subjects[0]['id'])
        self.assertEqual(saved_message, edited_message)
