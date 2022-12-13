import base64
from email.message import EmailMessage


class GmailService:
    """Class responsible for the interaction with the GmailAPI. Wraps a GmailAPI service object"""

    def __init__(self, build_function):
        """Constructor for the GmailService class, creates a new instance of the GmailService class

        Args:
            build_function (function): A function that builds a GmailAPI service object
        """

        self._service = None
        self._email = None
        self._build_function = build_function

    def build(self, creds):
        """Builds the GmailAPI service object

        Args:
            creds (Credentials): The credentials object to use for the service object
        """

        self._service = self._build_function('gmail', 'v1', credentials=creds)
        self._email = self._service.users()\
            .getProfile(userId='me').execute()['emailAddress']

    def destroy(self):
        """Destroys the GmailAPI service object"""

        self._service = None
        self._email = None

    def send(self, recipient, subject, body):
        """Sends an email through the GmailAPI

        Args:
            recipient (str): The recipient of the email
            subject (str): The subject of the email
            body (str): The body of the email
        """

        if not recipient:
            return
        message = self._create_message(recipient, subject, body)
        self._service.users().messages().send(
            userId='me', body=message
        ).execute()

    def _create_message(self, recipient, subject, body):
        mime_message = EmailMessage()
        mime_message.set_content(body)
        mime_message['From'] = self._email
        mime_message['To'] = recipient
        mime_message['Subject'] = subject

        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes())\
            .decode()

        return {
            'raw': encoded_message
        }

    def get_email(self):
        """Returns the email address of the user

        Returns:
            The email of the logged in user as a string
        """
        return self._email

    def get_service(self):
        """Returns the GmailAPI service object

        Returns:
            The GmailAPI service object
        """

        return self._service
