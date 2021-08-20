__author__ = "Haneen Mahdin"

from BitBuild.installer.InstallerWindow import InstallerWindow
from BitBuild.installer.installation import installation
from BitBuild.installer.utils.repair import repair
from BitBuild.installer.utils.uninstall import uninstall as _uninstall
from tkinter import messagebox

def uninstall():
    user_accept = messagebox.askyesno(title="Are you sure", message="Are you sure you want to uninstall")

    if user_accept:
        uninstall_run = _uninstall()
        
        if uninstall_run[0] != True:
            messagebox.showerror(title="Error", message=f"Failed to uninstall App\n Error: {uninstall_run[1].__name__}")
        else:
            messagebox.showinfo(title="Success", message="Uninstalled App successfully")
    else:
        messagebox.showinfo("Info", "Uninstallation was canceled.")


InstallerWindow(installation, repair, uninstall).app()