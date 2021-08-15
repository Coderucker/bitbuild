import re
from typing import Match

def match_platform(string: str, to_match_platform_list: list) -> tuple[Match[str], str]:
    """
    A Function to Match the preferred operating system.
    You need to provide a list of platforms inorder to match it.

    Example Usage:
    ```python
        match_platform("build_artifact_linux", ["linux", "android", "unix", "macos", "windows"])
    ```
    """

    for platform in to_match_platform_list:
        match_run = re.search(f"{platform}*", string)

        if match_run != None:
            return (match_run, True)