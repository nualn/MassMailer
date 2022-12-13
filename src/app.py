
class App:
    def __init__(self, auth, mail_service, parser, message_repository):
        self._auth = auth
        self._mail_service = mail_service
        self._parser = parser
        self._message_repository = message_repository

    def mass_send(self, message, rows):
        for row in rows:
            self._mail_service.send(
                self._parser.parse(message["to"], row),
                self._parser.parse(message["subject"], row),
                self._parser.parse(message["body"], row),
            )

    def login(self):
        self._auth.login()
        self._mail_service.build(self._auth.get_creds())

    def logout(self):
        self._auth.logout()
        self._mail_service.destroy()

    def get_email(self):
        return self._mail_service.get_email()

    def load_message(self, msg_id):
        return self._message_repository.get_by_id(msg_id)

    def save_message(self, message):
        self._message_repository.create(
            message["to"], message["subject"], message["body"])

    def edit_message(self, msg_id, message):
        self._message_repository.edit(
            msg_id, message["to"], message["subject"], message["body"])

    def list_messages(self):
        messages = self._message_repository.get_all_subjects()
        return messages
