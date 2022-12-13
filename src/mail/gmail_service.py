import base64
from email.message import EmailMessage


class GmailService:
    def __init__(self, build_function):
        self.service = None
        self.email = None
        self.build_function = build_function

    def build(self, creds):
        self.service = self.build_function('gmail', 'v1', credentials=creds)
        self.email = self.service.users()\
            .getProfile(userId='me').execute()['emailAddress']

    def destroy(self):
        self.service = None
        self.email = None

    def send(self, recipient, subject, body):
        if not recipient:
            return
        message = self._create_message(recipient, subject, body)
        self.service.users().messages().send(
            userId='me', body=message
        ).execute()

    def _create_message(self, recipient, subject, body):
        mime_message = EmailMessage()
        mime_message.set_content(body)
        mime_message['From'] = self.email
        mime_message['To'] = recipient
        mime_message['Subject'] = subject

        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes())\
            .decode()

        return {
            'raw': encoded_message
        }

    def get_email(self):
        return self.email

    def get_service(self):
        return self.service
