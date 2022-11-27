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

    def start(self):
        message_field = Message_field(self._root, self._state)
        message_field.pack()
        
        tbl = Tbl(self._root, self._state)
        tbl.pack()

        preview = Preview(self._root, self._state, parser)
        preview.pack()
        

