from tkinter import StringVar, OptionMenu, Frame, END


class Selector:
    """Selector component. Contains the selector menu."""

    def __init__(self, root, options):
        """Constructor for the Selector class, creates a new instance of the Selector class

        Args:
            root (Tk): The root Tk object
            options (list): The list of options to display in the selector
        """

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
        """Pack the frame"""
        self._frame.pack()

    def get_selected(self):
        """Get the selected option

        Returns:
            dict: The selected option
        """

        return self._selected

    def set_selected(self, obj):
        """Set the selected option

        Args:
            obj (dict): The selected option
        """

        self._variable.set(obj["subject"])
        self._selected = obj

    def refresh_options(self, options):
        """Refresh the options in the selector

        Args:
            options (list): The list of options to display in the selector
        """

        menu = self._menu["menu"]
        menu.delete(0, END)
        for message in [{"id": -1, "subject": "New"}, *options]:
            menu.add_command(
                label=message["subject"],
                command=lambda value=message: self.set_selected(value)
            )
