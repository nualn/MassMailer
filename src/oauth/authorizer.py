
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']


class Authorizer:
    def __init__(self):
        self.creds = None

    def is_authorized(self):
        return self.creds and self.creds.valid

    def login(self):
        try:
            if not self.creds and os.path.exists('token.json'):
                self.creds = Credentials.from_authorized_user_file(
                    'token.json', SCOPES)
            if not self.is_authorized():
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    self.creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w', encoding="utf-8") as token:
                    token.write(self.creds.to_json())
        except Exception:
            self.logout()

    def logout(self):
        self.creds = None
        if os.path.exists('token.json'):
            os.remove('token.json')

    def get_creds(self):
        return self.creds
