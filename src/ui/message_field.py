from tkinter import ttk, WORD, scrolledtext


class Message_field:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(self._root)

        to_label = ttk.Label(self._frame, text="To")
        to_label.pack()

        self.to_entry = ttk.Entry(self._frame, width=40, font=("Arial", 15))
        self.to_entry.pack()

        subj_label = ttk.Label(self._frame, text="Subject")
        subj_label.pack()

        self.subject_entry = ttk.Entry(
            self._frame, width=40, font=("Arial", 15))
        self.subject_entry.pack()
        self.message_entry = scrolledtext.ScrolledText(
            self._frame,
            wrap=WORD,
            width=40,
            height=10,
            font=("Arial",
                  15)
        )
        self.message_entry.pack(pady=20)

    def get_message(self):
        return {
            "to": self.to_entry.get(),
            "subject": self.subject_entry.get(),
            "body": self.message_entry.get("1.0", "end-1c")
        }

    def pack(self):
        self._frame.pack()
