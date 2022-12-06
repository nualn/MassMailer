import unittest
from unittest.mock import Mock
from app import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.auth = Mock()
        self.mail_service = Mock()
        self.mail_service.get_email.return_value = 'mock@email.com'
        self.parser = Mock()
        self.parser.parse.return_value = 'data'
        self.app = App(self.auth, self.mail_service, self.parser)

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
