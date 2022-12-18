from tkinter import ttk


class Loginout:
    """Loginout component. Contains the loginout button and the user label."""

    def __init__(self, root, app):
        """Constructor for the Loginout class, creates a new instance of the Loginout class

        Args:
            root (Tk): The root Tk object
            app (App): The App object
        """

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
        """Called when the loginout button is pressed. Changes the text of the button and calls the login or logout function in the App class."""
        if self.loginout_button['text'] == "Log In":
            self.loginout_button.configure(text="Log Out")
            self._app.login()
            self.user_label.configure(
                text=f"Logged in as: {self._app.get_email()}")
        else:
            self.loginout_button.configure(text="Log In")
            self._app.logout()
            self.user_label.configure(text="")
