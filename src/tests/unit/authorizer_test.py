import os
import unittest
from unittest.mock import Mock
from google_api.authorizer import Authorizer


# test Authorizer class
class AuthorizerTest(unittest.TestCase):
    def setUp(self):
        self.scope = ['https://www.googleapis.com/auth/gmail.compose']
        self.loaded_creds_mock = Mock()
        self.loaded_creds_mock.to_json.return_value = "{'some': 'credentials'}"
        self.loaded_creds_mock.valid = True
        self.request_mock = Mock()
        self.credentials_mock = Mock()
        self.credentials_mock.from_authorized_user_file.return_value = self.loaded_creds_mock
        self.flow_mock = Mock()
        self.flow_mock.from_client_secrets_file(
        ).run_local_server.return_value = self.loaded_creds_mock
        self.flow_mock.from_client_secrets_file.reset_mock()

        self.authorizer = Authorizer(
            self.request_mock, self.credentials_mock, self.flow_mock, 'test_token.json')

    def test_load_creds(self):
        self.authorizer._load_creds()
        self.credentials_mock.from_authorized_user_file.assert_called_once_with(
            'test_token.json', self.scope)

    def test_get_new_creds(self):
        self.authorizer._get_new_creds()
        self.flow_mock.from_client_secrets_file.assert_called_once_with(
            'credentials.json', ['https://www.googleapis.com/auth/gmail.compose'])
        self.flow_mock.from_client_secrets_file(
        ).run_local_server.assert_called_once_with(port=0)

    def test_is_authorized(self):
        self.assertFalse(self.authorizer.is_authorized())
        self.authorizer._load_creds()
        self.assertTrue(self.authorizer.is_authorized())

    def test_logout(self):
        self.authorizer._load_creds()
        self.authorizer._save_creds()
        self.assertIsNotNone(self.authorizer.get_creds())
        self.assertTrue(os.path.exists('test_token.json'))

        self.authorizer.logout()
        self.assertIsNone(self.authorizer.get_creds())
        self.assertFalse(os.path.exists('test_token.json'))

    def test_login(self):
        self.authorizer.logout()

        self.assertFalse(os.path.exists('test_token.json'))
        self.assertFalse(self.authorizer.is_authorized())

        self.authorizer.login()

        self.assertTrue(os.path.exists('test_token.json'))
        self.assertTrue(self.authorizer.is_authorized())
