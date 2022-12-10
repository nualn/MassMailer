from tkinter import ttk, WORD, scrolledtext, W, E

from ui.tbl import Tbl
from ui.message_field import Message_field
from ui.preview import Preview
from text_parser import parser
from ui.loginout import Loginout


class UI:
    def __init__(self, root, app):
        self._root = root
        self._app = app
        self._frame = ttk.Frame(self._root)
        self.pack = self._frame.pack

        loginout = Loginout(self._frame, self._app)
        loginout.grid(row=0, column=0, columnspan=3, sticky=E, pady=2)

        message_field = Message_field(self._frame, self._app)
        message_field.grid(row=1, column=0, sticky=W, pady=2)

        tbl = Tbl(self._frame)
        tbl.grid(row=1, column=1, sticky=W, pady=2)

        preview = Preview(
            self._frame,
            message_field.get_message,
            tbl.get_selected_row,
            parser
        )
        preview.grid(row=1, column=2, sticky=W, pady=2)

        send_button = ttk.Button(
            self._frame, text="Send all", command=lambda: self._app.mass_send(message_field.get_message(), tbl.get_all_rows())
        )
        send_button.grid(row=3, column=0, columnspan=3, sticky='NWES', pady=2)
