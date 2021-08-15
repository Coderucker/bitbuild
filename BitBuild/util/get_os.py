from sys import platform as __os_platform

def get_os() -> str:
    """
    Get the type of Operating System.
    """
    os_name = str(__os_platform)

    if os_name == "win32":
        return "windows"
    elif os_name == "darwin":
        return "macos"
    else:
        return "linux"