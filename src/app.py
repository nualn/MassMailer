
class App:
    """Class responsible for the application logic"""

    def __init__(self, auth, mail_service, parser, message_repository):
        """Constructor for the App class, creates a new instance of the App class
        
        Args:
            auth (Auth): An instance of the Auth class
            mail_service (MailService): An instance of the MailService class
            parser (Parser): An instance of the Parser class
            message_repository (MessageRepository): An instance of the MessageRepository class
        """
        self._auth = auth
        self._mail_service = mail_service
        self._parser = parser
        self._message_repository = message_repository

    def mass_send(self, message, rows):
        """Sends custom emails to recipients accordin to values in the rows list
        
        Args:
            message (dict): A dictionary with properties "to", "subject" and "body"
            rows (list): A list of dictionaries with values for the message
        """

        for row in rows:
            self._mail_service.send(
                self._parser.parse(message["to"], row),
                self._parser.parse(message["subject"], row),
                self._parser.parse(message["body"], row),
            )

    def login(self):
        """Logs in the user to the GmailAPI and builds the mail service"""

        self._auth.login()
        self._mail_service.build(self._auth.get_creds())

    def logout(self):
        """Logs out the user from the GmailAPI and destroys the mail service"""

        self._auth.logout()
        self._mail_service.destroy()

    def get_email(self):
        """Returns the email address of the user
        
        Returns: 
            The email of the logged in user as a string
        """

        return self._mail_service.get_email()

    def load_message(self, msg_id):
        """Loads a message from the database by its id

        Args:
            msg_id (int): The id of the message to load
        Returns: 
            A dictionary with properties "to", "subject", and "body"
        """

        return self._message_repository.get_by_id(msg_id)

    def save_message(self, message):
        """Saves a message to the database

        Args:
            message (dict): A dictionary with properties "to", "subject" and "body"
        """

        self._message_repository.create(
            message["to"], message["subject"], message["body"])

    def edit_message(self, msg_id, message):
        """Edits a message in the database

        Args:
            msg_id (int): The id of the message to edit
        """

        self._message_repository.edit(
            msg_id, message["to"], message["subject"], message["body"])

    def list_messages(self):
        """Returns a list of all messages in the database
        
        Returns: A list of dicts with properties "id" and "subject"
        """

        messages = self._message_repository.get_all_subjects()
        return messages
