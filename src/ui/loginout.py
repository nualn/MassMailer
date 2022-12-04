from tkinter import ttk


class Loginout:
    def __init__(self, root, auth):
        self._auth = auth
        self._root = root
        self._frame = ttk.Frame(self._root)

        self.user_label = ttk.Label(self._root, text="")
        self.user_label.pack()

        self.loginout_button = ttk.Button(self._frame, text="Log In",
                                          command=self.loginout_press)
        self.loginout_button.pack()

    def pack(self):
        self._frame.pack()

    def loginout_press(self):
        if self.loginout_button['text'] == "Log In":
            self.loginout_button.configure(text="Log Out")
            self._auth.login()
            self.user_label.configure(text="User email here")
        else:
            self.loginout_button.configure(text="Log In")
            self._auth.logout()
            self.user_label.configure(text="")
