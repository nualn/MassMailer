from tkinter import Tk
from mail.gmail_service import GmailService
from mail.mailer import Mailer
from ui.ui import UI
from oauth.authorizer import Authorizer

test_message = {
    'to': 'nuuttinikkola1+1@gmail.com',
    'subject': 'test',
    'body': 'test test test'
}


def main():
    window = Tk()
    window.title("MassMailer")
    window.geometry('500x1000')

    auth = Authorizer()
    # gmail = Gmail_service(auth.get_creds())
    # mailer = Mailer(gmail)

    user_interface = UI(window, auth)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
