from tkinter import StringVar, OptionMenu, Frame, END


class Selector:
    def __init__(self, root, options):
        self._root = root
        self._frame = Frame(self._root)
        self.grid = self._frame.grid

        self._variable = StringVar(self._frame)
        self._variable.set("New")  # default value
        self._selected = {"id": -1, "subject": "New"}

        self._menu = OptionMenu(self._frame, self._variable, "")
        self.refresh_options(options)
        self._menu.grid()

    def pack(self):
        self._frame.pack()

    def get_selected(self):
        return self._selected

    def set_selected(self, obj):
        self._variable.set(obj["subject"])
        self._selected = obj

    def refresh_options(self, options):
        menu = self._menu["menu"]
        menu.delete(0, END)
        for message in [{"id": -1, "subject": "New"}, *options]:
            menu.add_command(
                label=message["subject"],
                command=lambda value=message: self.set_selected(value)
            )
