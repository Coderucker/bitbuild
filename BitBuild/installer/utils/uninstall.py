import os
import sys
from pathlib import Path
from BitBuild.util.is_in_path import is_in_path

def uninstall():
    path = is_in_path()[1] if is_in_path()[1] != None else None

    if path != None and os.path.exists(path):
        os.rmdir(path)
        
        return True
    else:
        try:
            # Try uninstalling from a default path where the app is installed.
            path = f"{Path.home()}\\Applications\\BitBuild"
            return True
        except:
            return False
