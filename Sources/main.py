from Sources.lib.read_cache import read_cache
from Sources.lib.ignore_git import ignore_git
from Sources.internals.watchman.main import (DirectoryWatcher, FileWatcher)

read_cache()

def main():
    # Making cache.txt file ignored by git
    ignore_git()
    
    DirectoryWatcher("./").watch()


main()