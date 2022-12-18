from tkinter import ttk, WORD, scrolledtext, END, W
from ui.components.selector import Selector

FIELD_WIDTH = 10


class Message_field:
    """Message field component. Contains the message field and the save/load buttons."""

    def __init__(self, root, app):
        """Constructor for the Message_field class, creates a new instance of the Message_field class

        Args:
            root (Tk): The root Tk object
            app (App): The App object
        """

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

        to_label = ttk.Label(self._frame, text="To: ")
        to_label.grid(row=0, column=0, sticky=W, pady=2)

        self.to_entry = ttk.Entry(self._frame, width=30, font=("Arial", 11))
        self.to_entry.grid(
            row=0, column=1, columnspan=FIELD_WIDTH, sticky=W, pady=2)

        subj_label = ttk.Label(self._frame, text="Subject: ")
        subj_label.grid(row=1, column=0, sticky=W, pady=2)

        self.subject_entry = ttk.Entry(
            self._frame, width=30, font=("Arial", 11))
        self.subject_entry.grid(
            row=1, column=1, columnspan=FIELD_WIDTH, sticky=W, pady=2)

        body_label = ttk.Label(self._frame, text="Body: ")
        body_label.grid(row=2, column=0, sticky=W, pady=2)

        self.message_entry = scrolledtext.ScrolledText(
            self._frame,
            wrap=WORD,
            width=30,
            height=15,
            font=("Arial",
                  11)
        )
        self.message_entry.grid(
            row=2, column=1, columnspan=FIELD_WIDTH, rowspan=10, sticky=W, pady=2)

    def get_message(self):
        """Returns the message in the message field as a dictionary

        Returns:
            dict: The message in the message field as a dictionary
        """

        return {
            "to": self.to_entry.get(),
            "subject": self.subject_entry.get(),
            "body": self.message_entry.get("1.0", "end-1c")
        }

    def set_message(self, message):
        """Sets the message in the message field

        Args:
            message (dict): The message to set in the message field. Must be a dictionary with the keys "to", "subject" and "body"
        """

        self.to_entry.delete(0, END)
        self.subject_entry.delete(0, END)
        self.message_entry.delete("1.0", "end-1c")

        self.to_entry.insert(0, message["to"])
        self.subject_entry.insert(0, message["subject"])
        self.message_entry.insert("1.0", message["body"])

    def save_message(self):
        """Saves the message in the message field"""

        msg_id = self._selector.get_selected()["id"]
        message = self.get_message()
        if msg_id < 0:
            self._app.save_message(message)
        else:
            self._app.edit_message(msg_id, message)
        new_options = self._app.list_messages()
        self._selector.refresh_options(new_options)

    def load_message(self):
        """Loads the selected message into the message field"""

        selection = self._selector.get_selected()
        if selection["id"] < 0:
            return
        message = self._app.load_message(selection["id"])
        self.set_message(message)
