
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']


class Authorizer:
    """Class for authorizing the app to use Gmail API"""

    def __init__(self, request=Request, credentials=Credentials, flow=InstalledAppFlow):
        """Initialize the Authorizer class

        Args:
            request (Request): A request object for the Google API
            credentials (Credentials): A credentials object for the Google API
            flow (InstalledAppFlow): A flow object for the Google API
        """
        self._loaded_creds = None
        self._request = request
        self._credentials = credentials
        self._flow = flow

    def is_authorized(self):
        """Check if the user is authorized

        Returns:
            True if the user is authorized, False otherwise
        """
        return self._loaded_creds and self._loaded_creds.valid

    def _load_creds(self):
        self._loaded_creds = self._credentials.from_authorized_user_file(
            'token.json', SCOPES)

    def _get_new_creds(self):
        flow = self._flow.from_client_secrets_file(
            'credentials.json', SCOPES)
        self._loaded_creds = flow.run_local_server(port=0)

    def _save_creds(self):
        with open('token.json', 'w', encoding="utf-8") as token:
            token.write(self._loaded_creds.to_json())

    def login(self):
        """Logs in the user to the GmailAPI"""

        try:
            if not self._loaded_creds and os.path.exists('token.json'):
                self._load_creds()
            if not self.is_authorized():
                if self._loaded_creds\
                        and self._loaded_creds.expired\
                        and self._loaded_creds.refresh_token:
                    self._loaded_creds.refresh(self._request())
                else:
                    self._get_new_creds()
                self._save_creds()
        except Exception:
            self.logout()

    def logout(self):
        """Logs out the user from the GmailAPI by removing
           the authorized token from program memory and from disk"""

        self._loaded_creds = None
        if os.path.exists('token.json'):
            os.remove('token.json')

    def get_creds(self):
        """Returns the credentials of the user

        Returns:
            The credentials of the logged in user
        """

        return self._loaded_creds
