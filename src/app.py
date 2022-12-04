
class App:
    def __init__(self, auth, mail_service, parser):
        self._auth = auth
        self._mail_service = mail_service
        self._parser = parser

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
