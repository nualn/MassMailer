import unittest
from unittest.mock import Mock
from mail.gmail_service import GmailService


class TestGmailService(unittest.TestCase):
    def setUp(self):
        self.build_function = Mock()
        self.build_function().users().getProfile(userId='me').execute.return_value = {
            'emailAddress': 'test@gmail.com'
        }
        self.service = GmailService(self.build_function)

        self.body_encoded = 'Q29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1dGYtOCIKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdApNSU1FLVZlcnNpb246IDEuMApGcm9tOiB0ZXN0QGdtYWlsLmNvbQpUbzogcmVjZWlwaWVudEBnbWFpbC5jb20KU3ViamVjdDogc3ViamVjdAoKYm9keQo='

    def test_build(self):
        creds = {'some': 'credentials'}
        self.service.build(creds)
        self.assertIsNotNone(self.service.get_service())
        self.assertIsNotNone(self.service.get_email())

    def test_destroy(self):
        creds = {'some': 'credentials'}
        self.service.build(creds)
        self.service.destroy()
        self.assertIsNone(self.service.get_service())
        self.assertIsNone(self.service.get_email())

    def test_send(self):
        creds = {'some': 'credentials'}
        self.service.build(creds)

        self.service.send('receipient@gmail.com', 'subject', 'body')
        self.service.get_service().users().messages().send.assert_called_once_with(
            userId='me',
            body={'raw': self.body_encoded}
        )

    def test_create_message(self):
        self.service._email = 'test@gmail.com'
        message = self.service._create_message(
            'receipient@gmail.com', 'subject', 'body')
        self.assertEqual(message['raw'], self.body_encoded)

    def test_get_email(self):
        self.service._email = 'test@gmail.com'
        self.assertEqual(self.service.get_email(), 'test@gmail.com')
