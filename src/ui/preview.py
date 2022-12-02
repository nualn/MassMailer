from tkinter import ttk, WORD, scrolledtext


class Preview:
    def __init__(self, root, get_message, get_variables, parser):
        self._root = root
        self.get_message = get_message
        self.get_variables = get_variables
        self._parser = parser
        self._frame = ttk.Frame(self._root)

        self.preview_text = scrolledtext.ScrolledText(
            self._frame,
            state='disabled',
            wrap=WORD,
            width=40,
            height=10,
            font=("Arial",
                  15)
        )
        self.preview_text.pack()

        preview_button = ttk.Button(
            self._frame, text="Preview", command=self.get_preview)
        preview_button.pack()

    def get_preview(self):
        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0", "end-1c")
        self.preview_text.insert("1.0", self._parser.parse(
            self.get_message(),
            self.get_variables()
        ))
        self.preview_text.configure(state="disabled")

    def pack(self):
        self._frame.pack()
