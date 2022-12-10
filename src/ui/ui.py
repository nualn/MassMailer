from tkinter import ttk, WORD, scrolledtext

from ui.tbl import Tbl
from ui.message_field import Message_field
from ui.preview import Preview
from text_parser import parser
from ui.loginout import Loginout


class UI:
    def __init__(self, root, app):
        self._root = root
        self._app = app

    def start(self):

        loginout = Loginout(self._root, self._app)
        loginout.pack()

        message_field = Message_field(self._root, self._app)
        message_field.pack()

        tbl = Tbl(self._root)
        tbl.pack()

        preview = Preview(
            self._root,
            message_field.get_message,
            tbl.get_selected_row,
            parser
        )
        preview.pack()

        send_button = ttk.Button(
            self._root, text="Send all", command=lambda: self._app.mass_send(message_field.get_message(), tbl.get_all_rows())
        )
        send_button.pack()
