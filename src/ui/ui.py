from tkinter import ttk
from tkinter import *
from ui.tbl import Tbl
from tkinter import scrolledtext

from parser import parser

class UI:
    def __init__(self, root, state):
        self._root = root
        self._label_var = None
        self._state = state

    def start(self):
        message_frame = Frame(self._root)
        message_frame.pack()
        self.message_entry = scrolledtext.ScrolledText(message_frame, 
            wrap = WORD, 
            width = 40, 
            height = 10, 
            font = ("Arial",
                    15)
        )
        self.message_entry.pack(pady=20)


        self.message_entry.bind("<KeyRelease>", self.update_message)

        tbl_frame = Frame(self._root)
        tbl_frame.pack(pady=20)
        tbl = Tbl(tbl_frame, self._state)
        tbl.start()

        preview_frame = Frame(self._root)
        preview_frame.pack(pady=20)
        self.preview_text = scrolledtext.ScrolledText(preview_frame, 
            state='disabled',
            wrap = WORD, 
            width = 40, 
            height = 10, 
            font = ("Arial",
                    15)
        )
        self.preview_text.pack()

        preview_button = Button(preview_frame,text="Preview",command=self.get_preview)
        preview_button.pack()
        
    def get_preview(self):
        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0","end-1c")
        self.preview_text.insert("1.0",parser.parse(
            self._state.get_message(),
            self._state.get_headings(),
            self._state.get_selected()
        ))
        self.preview_text.configure(state="disabled")

    def update_message(self, _):
        self._state.set_message(self.message_entry.get("1.0","end-1c"))
