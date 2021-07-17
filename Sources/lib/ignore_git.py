"""
This file makes git ignore cache.txt while commiting
"""
import os
import re

def already_ignored():
    f = open(".gitignore").read()
    match_search = re.search("cache.txt*", f)

    if getattr(match_search, 'group', 'None') != "None" and match_search.group() != "":
        return True
    else:
        return False

def ignore_git():
    if os.path.exists(".gitignore"):
        if not already_ignored():
            f = open(".gitignore", "a")

            f.write("\n\n# Cache File by amberbuild \n*.cache.txt")

ignore_git()