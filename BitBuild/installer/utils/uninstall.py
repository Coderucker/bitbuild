import os
from posixpath import realpath
import sys
from pathlib import Path
from BitBuild.util.is_in_path import is_in_path

def uninstall():
    path = is_in_path()

    if path != None and os.path.exists(path):
        os.rmdir(path)
        
        return True
    else:
        # Try uninstalling from a default path where the app is installed.
        path = f"{Path.home()}\\Applications\\BitBuild"

        if os.path.exists(path):
            for content in os.listdir(path):
                real_content_path = os.path.join(path, content)

                os.remove(real_content_path)

        # Remove BitBuild Directory and Applications too
        bitbuild_dir_path = f"{Path.home()}\\Applications\\BitBuild"
        if os.path.exists(bitbuild_dir_path):
            os.rmdir(bitbuild_dir_path)

        application_path = f"{Path.home()}\\Applications"
        if os.path.exists(application_path) and len(os.listdir(bitbuild_dir_path)) == 1 and os.listdir(bitbuild_dir_path)[0] == "BitBuild":
            os.rmdir(application_path)
        
        print("Uninstalled app from path:", path)
        return True
