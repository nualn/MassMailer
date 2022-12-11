from tkintertable import TableCanvas
from tkinter import ttk


class Tbl:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(self._root)
        self.pack = self._frame.pack
        self.grid = self._frame.grid

        self._table = TableCanvas(self._frame)
        self._table.show()

    def get_all_rows(self):
        model = self._table.getModel()
        records = model.getAllCells().values()
        column_names = model.columnlabels
        return list(map(lambda rec: {column_names[i]: rec[i] for i in range(len(column_names))}, records))

    def get_selected_row(self):
        model = self._table.getModel()
        column_lables = model.columnlabels
        selected = self._table.get_currentRecord()
        res = {}
        for column_name in column_lables.keys():
            if column_name in selected:
                res[column_lables[column_name]] = selected[column_name]
        return res

