dummy_titles = ['1', '2', '3']
dummy_rows = [['foo', 'bar', 'baz'], ['boo', 'far', 'faz']]


class State:
    def __init__(self):
        self._headings = []
        self._rows = []
        self._selected = []
        self._message = ""
        self.set_headings(dummy_titles)
        self.set_rows(dummy_rows)

    # heading methods
    def set_headings(self, new_headings):
        self._headings = new_headings

    def add_heading(self, heading):
        self._headings.append(heading)

    def get_headings(self):
        return self._headings

    def remove_heading(self, index):
        self._headings.pop(index)

    def update_heading(self, index, new_heading):
        self._headings[index] = new_heading

    # row methods
    def set_rows(self, new_rows):
        self._rows = new_rows

    def add_row(self, row):
        self._rows.append(row)

    def get_rows(self):
        return self._rows

    def remove_row(self, index):
        self._rows.pop(index)

    def update_row(self, index, new_row):
        self._rows[index] = new_row

    # selected methods
    def set_selected(self, row):
        self._selected = row

    def get_selected(self):
        return self._selected

    # message methods
    def set_message(self, new_message):
        self._message = new_message

    def get_message(self):
        return self._message
