from tkintertable import TableCanvas
from tkinter import ttk


class Tbl:
    """Table component. Contains the table and the functions to get the selected row and all rows."""

    def __init__(self, root):
        """Constructor for the Tbl class, creates a new instance of the Tbl class

        Args:
            root (Tk): The root Tk object
        """

        self._root = root
        self._frame = ttk.Frame(self._root)
        self.pack = self._frame.pack
        self.grid = self._frame.grid

        self._table = TableCanvas(self._frame)
        self._table.show()

    def get_all_rows(self):
        """Returns all rows in the table as a list of dictionaries

        Returns:
            A list of dictionaries
        """

        model = self._table.getModel()
        records = model.getAllCells().values()
        model = self._table.getModel()
        column_lables = list(model.columnlabels.values())
        return list(map(lambda rec: {column_lables[i]: rec[i] for i in range(len(column_lables))}, records))

    def get_selected_row(self):
        """Returns the selected row in the table as a dictionary

        Returns:
            A dictionary with the selected row in the form of {column_name: value}
        """

        model = self._table.getModel()
        column_lables = model.columnlabels
        selected = self._table.get_currentRecord()
        res = {}
        for column_name in column_lables.keys():
            if column_name in selected:
                res[column_lables[column_name]] = selected[column_name]
        return res
