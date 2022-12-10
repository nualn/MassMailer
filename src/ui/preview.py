from tkinter import ttk, WORD, scrolledtext, END, W


class Preview:
    def __init__(self, root, get_message, get_variables, parser):
        self._root = root
        self.get_message = get_message
        self.get_variables = get_variables
        self._parser = parser
        self._frame = ttk.Frame(self._root)
        self.pack = self._frame.pack
        self.grid = self._frame.grid

        to_label = ttk.Label(self._frame, text="To")
        to_label.grid(row=0, column=0, sticky=W, pady=2)

        self.preview_to = ttk.Entry(
            self._frame, width=30, font=("Arial", 15), state="disabled")
        self.preview_to.grid(row=0, column=1, sticky=W, pady=2)

        subj_label = ttk.Label(self._frame, text="Subject")
        subj_label.grid(row=1, column=0, sticky=W, pady=2)

        self.preview_subject = ttk.Entry(
            self._frame, width=30, font=("Arial", 15), state="disabled")
        self.preview_subject.grid(row=1, column=1, sticky=W, pady=2)

        body_label = ttk.Label(self._frame, text="Body:")
        body_label.grid(row=2, column=0, sticky=W, pady=2)

        self.preview_text = scrolledtext.ScrolledText(
            self._frame,
            state='disabled',
            wrap=WORD,
            width=30,
            height=15,
            font=("Arial",
                  15)
        )
        self.preview_text.grid(row=2, column=1, rowspan=10, sticky=W, pady=2)

        preview_button = ttk.Button(
            self._frame, text="Preview", command=self.get_preview)
        preview_button.grid(row=12, column=1, sticky=W, pady=2)

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
