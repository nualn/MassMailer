from tkinter import ttk, WORD, scrolledtext


class Message_field:
    def __init__(self, root, state):
        self._root = root
        self._state = state
        self._frame = ttk.Frame(self._root)

        self.message_entry = scrolledtext.ScrolledText(
            self._frame,
            wrap=WORD,
            width=40,
            height=10,
            font=("Arial",
                  15)
        )
        self.message_entry.pack(pady=20)

        self.message_entry.bind("<KeyRelease>", self.update_message)

    def update_message(self, _):
        self._state.set_message(self.message_entry.get("1.0", "end-1c"))

    def pack(self):
        self._frame.pack()
