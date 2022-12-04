from tkinter import ttk, WORD, scrolledtext, END


class Preview:
    def __init__(self, root, get_message, get_variables, parser):
        self._root = root
        self.get_message = get_message
        self.get_variables = get_variables
        self._parser = parser
        self._frame = ttk.Frame(self._root)

        to_label = ttk.Label(self._frame, text="To")
        to_label.pack()

        self.preview_to = ttk.Entry(
            self._frame, width=40, font=("Arial", 15), state="disabled")
        self.preview_to.pack()

        subj_label = ttk.Label(self._frame, text="Subject")
        subj_label.pack()

        self.preview_subject = ttk.Entry(
            self._frame, width=40, font=("Arial", 15), state="disabled")
        self.preview_subject.pack()

        self.preview_text = scrolledtext.ScrolledText(
            self._frame,
            state='disabled',
            wrap=WORD,
            width=40,
            height=5,
            font=("Arial",
                  15)
        )
        self.preview_text.pack()

        preview_button = ttk.Button(
            self._frame, text="Preview", command=self.get_preview)
        preview_button.pack()

    def get_preview(self):
        message = self.get_message()
        variables = self.get_variables()

        self.preview_to.configure(state="normal")
        self.preview_subject.configure(state="normal")
        self.preview_text.configure(state="normal")

        self.preview_to.delete(0, END)
        self.preview_subject.delete(0, END)
        self.preview_text.delete("1.0", "end-1c")

        self.preview_to.insert(0, self._parser.parse(message["to"], variables))
        self.preview_subject.insert(
            0, self._parser.parse(message["subject"], variables))
        self.preview_text.insert(
            "1.0", self._parser.parse(message["body"], variables))

        self.preview_to.configure(state="disabled")
        self.preview_subject.configure(state="disabled")
        self.preview_text.configure(state="disabled")

    def pack(self):
        self._frame.pack()
