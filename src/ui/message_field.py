from tkinter import ttk, WORD, scrolledtext, END, W
from ui.selector import Selector
from ast import literal_eval

FIELD_WIDTH = 10


class Message_field:
    def __init__(self, root, app):
        self._root = root
        self._frame = ttk.Frame(self._root)
        self._app = app
        self.pack = self._frame.pack
        self.grid = self._frame.grid

        selector_frame = ttk.Frame(self._frame)
        selector_frame.grid(row=12, column=1, columnspan=3, sticky=W, pady=2)

        self._selector = Selector(selector_frame, self._app.list_messages())
        self._selector.grid(row=0, column=0, sticky=W, pady=2)

        save_button = ttk.Button(
            selector_frame, text="Save", command=self.save_message)
        save_button.grid(row=0, column=1, sticky=W, pady=2)
        load_button = ttk.Button(
            selector_frame, text="Load", command=self.load_message)
        load_button.grid(row=0, column=2, sticky=W, pady=2)

        to_label = ttk.Label(self._frame, text="To:")
        to_label.grid(row=0, column=0, sticky=W, pady=2)

        self.to_entry = ttk.Entry(self._frame, width=30, font=("Arial", 15))
        self.to_entry.grid(
            row=0, column=1, columnspan=FIELD_WIDTH, sticky=W, pady=2)

        subj_label = ttk.Label(self._frame, text="Subject:")
        subj_label.grid(row=1, column=0, sticky=W, pady=2)

        self.subject_entry = ttk.Entry(
            self._frame, width=30, font=("Arial", 15))
        self.subject_entry.grid(
            row=1, column=1, columnspan=FIELD_WIDTH, sticky=W, pady=2)

        body_label = ttk.Label(self._frame, text="Body:")
        body_label.grid(row=2, column=0, sticky=W, pady=2)

        self.message_entry = scrolledtext.ScrolledText(
            self._frame,
            wrap=WORD,
            width=30,
            height=15,
            font=("Arial",
                  15)
        )
        self.message_entry.grid(
            row=2, column=1, columnspan=FIELD_WIDTH, rowspan=10, sticky=W, pady=2)

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
