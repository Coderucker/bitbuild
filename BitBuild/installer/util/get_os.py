from sys import platform as __os_platform
from typing import (Tuple)

def get_os() -> Tuple(str, __os_platform):
    """
    Get the type of Operating System.
    """
    os_name = str(__os_platform)

    if os_name == "win32":
        return ("Windows", os_name)
    else:
        return ("Unix", os_name)