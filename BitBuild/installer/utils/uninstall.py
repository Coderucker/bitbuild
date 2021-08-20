import os
from pathlib import Path
from BitBuild.util.is_in_path import is_in_path

def uninstall():
    """
    Returns `True` if successful.
    If error occured returns a Tuple with the first element as `False` and 
    Second element with the type of error.
    """
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

        try:
            application_path = f"{Path.home()}\\Applications"
            if os.path.exists(application_path) and len(os.listdir(bitbuild_dir_path)) == 1 and os.listdir(bitbuild_dir_path)[0] == "BitBuild":
                os.rmdir(application_path)
            
            print("Uninstalled app from path:", path)
            return True
        except FileNotFoundError:
            # Return if error occured
            return (False, FileNotFoundError)
