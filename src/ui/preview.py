from tkinter import ttk, WORD, scrolledtext

class Preview:
    def __init__(self, root, state, parser):
        self._root = root
        self._state = state
        self._parser = parser

        preview_frame = ttk.Frame(self._root)
        preview_frame.pack(pady=20)
        self.preview_text = scrolledtext.ScrolledText(preview_frame, 
            state='disabled',
            wrap = WORD, 
            width = 40, 
            height = 10, 
            font = ("Arial",
                    15)
        )
        self.preview_text.pack()

        preview_button = ttk.Button(preview_frame,text="Preview",command=self.get_preview)
        preview_button.pack()

    def get_preview(self):
        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0","end-1c")
        self.preview_text.insert("1.0",self._parser.parse(
            self._state.get_message(),
            self._state.get_headings(),
            self._state.get_selected()
        ))
        self.preview_text.configure(state="disabled")