from tkinter import *
from ctypes import windll
from typing import Callable

# Fix blurry issue on windows
windll.shcore.SetProcessDpiAwareness(1)

class InstallerWindow:
    """
    Creates an Instance of Installer Window which shows the options to do whatever.
    """
    
    def __init__(self, installer_func: Callable, repair_func: Callable, uninstall_func: Callable) -> None:   
        app = Tk()
        app.title("BitBuild Setup")
        app.geometry("600x600")

        main_message = Label(app, text="Setup for BitBuild", font=("SF Pro Display", 24, "bold"), pady=10, padx=30)
        main_message.grid(row=0, column=0)

        main_desc = Label(app, text="Click Continue to continue installation", font=("SF Pro Display", 12), pady=10, padx=30)
        main_desc.grid(row=1, column=0)

        continue_btn = Button(app, text="Continue", font=("SF Pro Display", 12), bg="#c4c4c4", border=0, padx=10, pady=7, command=installer_func)
        continue_btn.place(x=50, y=500)

        def destroy_window():
            """
            Destroys a window instance
            """
            app.destroy()


        exit_button = Button(app, text="Exit", font=("SF Pro Display", 12), bg="#FF0000", padx=20, pady=7, border=0, fg="#fff", command=destroy_window)
        exit_button.place(x=200, y=500)

        app.resizable(False, False)

        app.mainloop()