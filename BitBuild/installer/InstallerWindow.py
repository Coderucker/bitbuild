from BitBuild.installer.utils.repair import repair
from BitBuild.installer.installation import installation
from tkinter import *
from ctypes import windll
from typing import Callable

# Fix blurry issue on windows
windll.shcore.SetProcessDpiAwareness(1)

def destroy_window(app: Tk):
    """
    Destroys a window instance
    """
    app.destroy()


class InstallerWindow:
    """
    Creates an Instance of Installer Window which shows the options to do whatever.
    """

    def __init__(self, installer_func: Callable, repair_func: Callable, uninstall_func: Callable) -> None:
        self.installer_func = installer_func
        self.repair_func = repair_func
        self.uninstall_func = uninstall_func

    def app(self):
        """
        Starts the app when you calls this functions
        """

        app = Tk()
        app.title("BitBuild Setup")
        app.geometry("600x600")

        def read_license() -> str:
            license = open("LICENSE").read(1000)

            return license

        def button(master, text, command=None, width=None):
            return Button(master, text=text, font=(
            "SF Pro Display", 12), bg="#d4d4d4", border=0, command=command, width=width)

        def openContinueWindow():
            """
            Opens the continue window
            """
            root = Tk()

            root.title("Installation Configuration")
            root.geometry("700x700")
            root.resizable(False, False)

            label = Label(root, text="Install", font=("SF Pro Display", 20, "bold"), pady=20)
            label.pack()

            license = read_license()

            license_text = Label(root, text=license, bg="#fff", font=("SF Pro Display", 10))
            license_text.pack()

            status = Label(root, text="Installing from Github Releases", font=("SF Pro Display", 12))

            def install():
                license_text.destroy()

                status.pack()
                
                install_run = installation()

                if install_run == 101:
                    status.configure(text="Failed to install! \n No Internet Connection", fg="#ff0000")

            button_install = button(root, text="Install", width=20, command=install)
            button_install.place(x=250, y=600)
            
            # Destroy main app after loading the new window content
            app.destroy()
        
        def openRepairWindow():
            """
            Opens the repair window
            """
            root = Tk()

            root.title("Repair Installation")
            root.geometry("500x500")
            root.resizable(False, False)
            root.configure(pady=20)

            label = Label(root, text="Repair BitBuild🛠️", font=("SF Pro Display", 20, "bold"), pady=20)
            label.pack()

            status = Label(root, text="Repairing", font=("SF Pro Display", 14))

            def repair_event():
                status.pack()

                repair_run = repair()

                if repair_run != True:
                    status.configure(text="Repair Failed❌")

            button_repair = button(root, text="Repair", width=20, command=repair_event)
            button_repair.pack(side="bottom")
            
            # Destroy main app after loading the new window content
            app.destroy()
        

        main_message = Label(app, text="Setup for BitBuild", font=(
            "SF Pro Display", 24, "bold"), pady=10, padx=30)
        main_message.grid(row=0, column=0)

        main_desc = Label(app, text="Click Continue to continue installation", font=(
            "SF Pro Display", 12), pady=10, padx=30)
        main_desc.grid(row=1, column=0)

        continue_btn = Button(app, text="Continue", font=(
            "SF Pro Display", 12), bg="#c4c4c4", border=0, padx=10, pady=7, command=openContinueWindow)
        continue_btn.place(x=50, y=500)

        reset_button = Button(app, text="Reset settings", font=(
            "SF Pro Display", 12), bg="#166edc", padx=20, pady=7, border=0, fg="#fff", command=openRepairWindow)
        reset_button.place(x=180, y=500)

        uninstall_button = Button(app, text="Uninstall", font=(
            "SF Pro Display", 12), bg="#FF0000", padx=20, pady=7, border=0, fg="#fff", command=self.uninstall_func)
        uninstall_button.place(x=380, y=500)

        app.resizable(False, False)

        app.mainloop()
