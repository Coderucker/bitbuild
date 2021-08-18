import os
import sys
from BitBuild.util.get_os import get_os
from BitBuild.util.is_in_path import is_in_path

def repair():
    env_var_path = is_in_path()

    if env_var_path != None and os.path.exists(env_var_path):
        print("No issues found!")
        return True
    else:
        return False