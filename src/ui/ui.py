from tkinter import ttk, WORD, scrolledtext

from ui.tbl import Tbl
from ui.message_field import Message_field
from ui.preview import Preview
from text_parser import parser


class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        message_field = Message_field(self._root)
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
