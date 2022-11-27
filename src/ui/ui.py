from tkinter import ttk, WORD, scrolledtext

from ui.tbl import Tbl
from ui.message_field import Message_field
from ui.preview import Preview
from parser import parser

class UI:
    def __init__(self, root, state):
        self._root = root
        self._label_var = None
        self._state = state

        message_field = Message_field(self._root, self._state)
        tbl_frame = ttk.Frame(self._root)
        tbl_frame.pack(pady=20)
        tbl = Tbl(tbl_frame, self._state)
        tbl.start()

        preview = Preview(self._root, self._state, parser)
        

