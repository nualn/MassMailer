from tkinter import Tk
from googleapiclient.discovery import build
from app import App
from mail.gmail_service import GmailService
from database.message_repository import message_repository
from ui.ui import UI
from oauth.authorizer import Authorizer
from text_parser import parser

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
    gmail = GmailService(build)
    app = App(auth, gmail, parser, message_repository)

    user_interface = UI(window, app)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
