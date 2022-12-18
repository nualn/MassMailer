import unittest
from unittest.mock import Mock
from app.app import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.auth = Mock()
        self.mail_service = Mock()
        self.mail_service.get_email.return_value = 'mock@email.com'
        self.parser = Mock()
        self.parser.parse.return_value = 'data'
        self.message_repository = Mock()
        self.app = App(self.auth, self.mail_service,
                       self.parser, self.message_repository)

    def test_mass_send(self):
        message = {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        }
        rows = [{'data': 'data1'}, {'data': 'data2'}, {'data': 'data3'}]
        self.app.mass_send(message, rows)

        self.assertEqual(self.parser.parse.call_count, 9)
        self.assertEqual(self.mail_service.send.call_count, 3)

    def test_login(self):
        self.app.login()

        self.auth.login.assert_called_once()
        self.mail_service.build.assert_called_once()

    def test_logout(self):
        self.app.logout()

        self.auth.logout.assert_called_once()
        self.mail_service.destroy.assert_called_once()

    def test_get_email(self):
        self.assertEqual(self.app.get_email(), 'mock@email.com')

    def test_load_message(self):
        self.message_repository.get_by_id.return_value = {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        }
        self.assertEqual(self.app.load_message(1), {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        })
        self.message_repository.get_by_id.assert_called_once_with(1)

    def test_save_message(self):
        message = {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        }
        self.app.save_message(message)

        self.message_repository.create.assert_called_once_with(
            'to', 'subject', 'body')

    def test_edit_message(self):
        message = {
            'to': 'to',
            'subject': 'subject',
            'body': 'body'
        }
        self.app.edit_message(1, message)

        self.message_repository.edit.assert_called_once_with(
            1, 'to', 'subject', 'body')

    def test_list_messages(self):
        self.message_repository.get_all_subjects.return_value = [
            {'id': 1, 'subject': 'subject1'},
            {'id': 2, 'subject': 'subject2'},
            {'id': 3, 'subject': 'subject3'}
        ]
        self.assertEqual(self.app.list_messages(), [
            {'id': 1, 'subject': 'subject1'},
            {'id': 2, 'subject': 'subject2'},
            {'id': 3, 'subject': 'subject3'}
        ])
        self.message_repository.get_all_subjects.assert_called_once()
