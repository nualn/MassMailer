from tkinter import ttk


class Loginout:
    def __init__(self, root, app):
        self._app = app
        self._root = root
        self._frame = ttk.Frame(self._root)
        self.grid = self._frame.grid
        self.pack = self._frame.pack

        self.loginout_button = ttk.Button(
            self._frame, text="Log In", command=self.loginout_press)
        self.loginout_button.pack(side='right')

        self.user_label = ttk.Label(self._frame, text="")
        self.user_label.pack(side='right')

    def loginout_press(self):
        if self.loginout_button['text'] == "Log In":
            self.loginout_button.configure(text="Log Out")
            self._app.login()
            self.user_label.configure(
                text=f"Logged in as: {self._app.get_email()}")
        else:
            self.loginout_button.configure(text="Log In")
            self._app.logout()
            self.user_label.configure(text="")
