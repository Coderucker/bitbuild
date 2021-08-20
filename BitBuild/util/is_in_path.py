import os
from BitBuild.util.get_os import get_os

def is_in_path():
    """
    Returns a tuple with the first element with a value of boolean
    whether if the env var exists. And the second element with path to env if the 
    first was true.
    """
    VARS = os.environ["PATH"].split(";")

    for var in VARS:
        if var.endswith("bitbuild.exe" if get_os() == "windows" else "bitbuild"):
            return var
    else:
        # Return false if not found
        return None