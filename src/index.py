from tkinter import Tk
from ui.ui import UI
from state import State

def main():
    window = Tk()
    window.title("MassMailer")
    window.geometry('500x500')

    state = State()

    ui = UI(window, state)

    window.mainloop()

if __name__ == "__main__":
    main()