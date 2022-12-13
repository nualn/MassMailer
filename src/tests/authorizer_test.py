import unittest
from unittest.mock import Mock
from google_api.authorizer import Authorizer


# test Authorizer class
class AuthorizerTest(unittest.TestCase):
    def setUp(self):
        self.scope = ['https://www.googleapis.com/auth/gmail.compose']
        self.loaded_creds_mock = Mock()
        self.loaded_creds_mock.valid = True
        self.refresher_mock = Mock()
        self.request_mock = Mock()
        self.credentials_mock = Mock()
        self.credentials_mock.from_authorized_user_file.return_value = self.loaded_creds_mock
        self.flow_mock = Mock()
        self.flow_mock.from_client_secrets_file.return_value = self.refresher_mock

        self.authorizer = Authorizer(
            self.request_mock, self.credentials_mock, self.flow_mock)

    def test_load_creds(self):
        self.authorizer._load_creds()
        self.credentials_mock.from_authorized_user_file.assert_called_once_with(
            'token.json', self.scope)

    def test_get_new_creds(self):
        self.authorizer._get_new_creds()
        self.flow_mock.from_client_secrets_file.assert_called_once_with(
            'credentials.json', ['https://www.googleapis.com/auth/gmail.compose'])
        self.refresher_mock.run_local_server.assert_called_once_with(port=0)

    def test_is_authorized(self):
        self.assertFalse(self.authorizer.is_authorized())
        self.authorizer._load_creds()
        self.assertTrue(self.authorizer.is_authorized())
