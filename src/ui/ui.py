from tkinter import ttk, W, E

from ui.components.tbl import Tbl
from ui.components.message_field import Message_field
from ui.components.preview import Preview
from utils.text_parser import parser
from ui.components.loginout import Loginout


class UI:
    """Main UI class. Contains all UI components and their positioning."""

    def __init__(self, root, app):
        """Constructor for the UI class, creates a new instance of the UI class

        Args:
            root (Tk): The root Tk object
            app (App): The App object

        """

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
