import os

from BitBuild.installer.installation import installation
from BitBuild.util.is_in_path import is_in_path

def before_repair():
    """
    `Warning`: Do not import this
    """

def repair():
    # Catch Errors
    return True if is_in_path() != None and os.path.exists(is_in_path()) else before_repair()