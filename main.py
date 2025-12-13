import tkinter as tk
from gui import TripGUI

def main():
    root = tk.Tk()
    app = TripGUI(root)

    def on_close():
        app.save_data()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    main()
