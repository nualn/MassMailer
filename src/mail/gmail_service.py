import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GmailService:
    def __init__(self, creds):
        self.creds = creds
        try:
            self.service = build('gmail', 'v1', credentials=self.creds)
            self.email = self.service.users()\
                .getProfile(userId='me').execute()['emailAddress']
            print(self.email)
        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')

    def send(self, receipent, subject, body):
        try:
            message = self._create_message(receipent, subject, body)
            self.service.users().messages().send(
                userId='me', body=message
            ).execute()
        except HttpError as error:
            print(f'An error occurred: {error}')

    def _create_message(self, receipent, subject, body):
        mime_message = EmailMessage()
        mime_message.set_content(body)
        mime_message['From'] = self.email
        mime_message['To'] = receipent
        mime_message['Subject'] = subject

        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes())\
            .decode()

        return {
            'raw': encoded_message
        }
