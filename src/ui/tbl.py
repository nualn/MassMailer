from tkinter import ttk, NO, CENTER, END

class Tbl:
    def __init__(self, root, state):
        self._root = root
        self._state = state
        self._entry_fields = []
        self._frame = ttk.Frame(self._root)

        self.tbl = ttk.Treeview(self._frame)
        self.tbl.pack()
        self.tbl.bind('<ButtonRelease-1>', self.select_row)
        self.tbl.bind('<KeyRelease>', self.select_row)

        # define columns
        self.tbl['columns'] = self._state.get_headings()
        self.tbl.column("#0", width=0, stretch=NO)
        self.tbl.heading("#0",text="",anchor=CENTER)
        for heading in self._state.get_headings():
            self.tbl.column(heading, anchor=CENTER, width=80)
            self.tbl.heading(heading,text=heading,anchor=CENTER)

        # add rows
        for i, row in enumerate(self._state.get_rows()):
            self.tbl.insert(parent='',index='end', values=row)


        frame = ttk.Frame(self._frame)
        frame.pack(pady=20)

        for i, field in enumerate(self._state.get_headings()):
            label = ttk.Label(frame,text=field)
            entry = ttk.Entry(frame)
            label.grid(row=0,column=i)
            entry.grid(row= 1, column=i)
            self._entry_fields.append(entry)

        new_button = ttk.Button(frame,text="New ",command=self.insert_row)
        new_button.grid(row=2, column=0)

        edit_button = ttk.Button(frame,text="Update ",command=self.update_row)
        edit_button.grid(row=2, column=1)

        clear_button = ttk.Button(frame, text="Clear ", command=self.clear_fields)
        clear_button.grid(row=2, column=2)

    def select_row(self, _):
        self.clear_fields()
        selected=self.tbl.focus()
        values = self.tbl.item(selected,'values')
        self._state.set_selected(values)
        for i, entry in enumerate(self._entry_fields):
            entry.insert(0,values[i])

    def update_row(self):
        selected=self.tbl.focus()
        #save new data 
        self.tbl.item(selected,text="",values=list(map(lambda entry: entry.get(), self._entry_fields)))
        self.clear_fields()
        
    def insert_row(self):
        self.tbl.insert(parent='',index='end',values=list(map(lambda entry: entry.get(), self._entry_fields)))
        self.clear_fields()

    def clear_fields(self):
        for entry in self._entry_fields:
            entry.delete(0,END)

    def pack(self):
        self._frame.pack()