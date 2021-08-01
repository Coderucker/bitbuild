from os import system
from subprocess import (check_output, run)

def add_to_path(path: str):
    # First entering in to system dir for windows
    run(["cd", "c:\windows\system"])
    run_output = check_output(["SetX", "PATH" , f"{path};%PATH%", "\m"])

    print(run_output)

add_to_path(input("Enter path to add: "))