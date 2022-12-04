from tkintertable import TableCanvas, TableModel
from tkinter import ttk, BOTH


class Tbl:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(self._root)

        self._table = TableCanvas(self._frame)
        self._table.show()

    def pack(self):
        self._frame.pack()

    def get_all_rows(self):
        model = self._table.getModel()
        records = model.getAllCells().values()
        column_names = model.columnNames
        return list(map(lambda rec: {column_names[i]: rec[i] for i in range(len(column_names))}, records))

    def get_selected_row(self):
        return self._table.get_currentRecord()
