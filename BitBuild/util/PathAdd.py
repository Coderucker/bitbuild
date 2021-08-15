from BitBuild.util.get_os import get_os
from subprocess import (check_output, run)

def add_to_path_win32(path: str):
    # First entering in to system dir for windows
    run(["cd", "c:\windows\system"])
    run_output = check_output(["SetX", "PATH" , f"{path};%PATH%", "\m"])

    return run_output

def add_to_path_unix(path: str):
    # First entering in to $HOME dir for unix, linux and osx systems
    run(["cd", "$HOME"])
    run_output = check_output(["export", f"PATH={path}:$PATH"])

    return run_output

class PathAdd:
    """
    This is a class which adds a program to path.
    Works perfectly🤠 with Windows, Linux and OSX Systems.
    This is used by BitBuild to add the `bitbuild.exe` to environment path.
    """
    os = get_os()

    def __init__(self):
        if self.os[0] == "Windows":
            add_to_path_win32("./exec") # NOTE: replace with original path
        else:
            add_to_path_unix("./exec") # NOTE: replace with original path