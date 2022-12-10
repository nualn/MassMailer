from tkinter import ttk, WORD, scrolledtext, END
from ui.selector import Selector
from ast import literal_eval


class Message_field:
    def __init__(self, root, app):
        self._root = root
        self._frame = ttk.Frame(self._root)
        self._app = app

        self._selector = Selector(self._frame, self._app.list_messages())
        self._selector.pack()

        save_button = ttk.Button(
            self._frame, text="Save", command=self.save_message)
        save_button.pack()
        load_button = ttk.Button(
            self._frame, text="Load", command=self.load_message)
        load_button.pack()

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
            height=5,
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

    def set_message(self, message):
        self.to_entry.delete(0, END)
        self.subject_entry.delete(0, END)
        self.message_entry.delete("1.0", "end-1c")

        self.to_entry.insert(0, message["to"])
        self.subject_entry.insert(0, message["subject"])
        self.message_entry.insert("1.0", message["body"])

    def save_message(self):
        msg_id = self._selector.get_selected()["id"]
        message = self.get_message()
        if msg_id < 0:
            self._app.save_message(message)
        else:
            self._app.edit_message(msg_id, message)
        new_options = self._app.list_messages()
        self._selector.refresh_options(new_options)

    def load_message(self):
        selection = self._selector.get_selected()
        if selection["id"] < 0:
            return
        message = self._app.load_message(selection["id"])
        self.set_message(message)

    def pack(self):
        self._frame.pack()
